import os

import torch
from torch.optim import AdamW
from torch.utils.data import DataLoader, random_split
from transformers import T5ForConditionalGeneration, T5Tokenizer, get_scheduler
from dataset import NotesDataset

# ─── Config ────────────────────────────────────────────────
MODEL_NAME    = "t5-small"       # small = faster, use t5-base for better quality
SCRIPT_DIR    = os.path.dirname(os.path.abspath(__file__))
DATA_PATH     = os.path.join(SCRIPT_DIR, "..", "data", "notes_dataset.json")
SAVE_PATH     = os.path.join(SCRIPT_DIR, "..", "model")
EPOCHS        = 10                # more epochs for better convergence
BATCH_SIZE    = 4
LR            = 3e-4
MAX_INPUT     = 128
MAX_TARGET    = 256
VAL_SPLIT     = 0.1              # 10% for validation
# ───────────────────────────────────────────────────────────

def train():
    torch.manual_seed(42)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(42)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    # Load tokenizer and model
    print("Loading T5 model and tokenizer...")
    tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME)
    if tokenizer.pad_token is None:
        tokenizer.add_special_tokens({"pad_token": "<pad>"})

    model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME).to(device)
    model.config.pad_token_id = tokenizer.pad_token_id
    if len(model.get_input_embeddings().weight) != len(tokenizer):
        model.resize_token_embeddings(len(tokenizer))

    # Load dataset and split
    full_dataset = NotesDataset(DATA_PATH, tokenizer, MAX_INPUT, MAX_TARGET)
    val_size = max(1, int(len(full_dataset) * VAL_SPLIT))
    train_size = len(full_dataset) - val_size
    train_dataset, val_dataset = random_split(full_dataset, [train_size, val_size])

    train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
    val_loader   = DataLoader(val_dataset,   batch_size=BATCH_SIZE)

    # Optimizer and scheduler
    optimizer = AdamW(model.parameters(), lr=LR)
    total_steps = len(train_loader) * EPOCHS
    scheduler = get_scheduler("linear", optimizer=optimizer,
                               num_warmup_steps=total_steps // 10,
                               num_training_steps=total_steps)

    best_val_loss = float("inf")

    for epoch in range(EPOCHS):
        # ── Training ──
        model.train()
        total_train_loss = 0
        for batch in train_loader:
            input_ids      = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
            labels         = batch["labels"].to(device)

            outputs = model(input_ids=input_ids,
                            attention_mask=attention_mask,
                            labels=labels)
            loss = outputs.loss

            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            scheduler.step()

            total_train_loss += loss.item()

        avg_train_loss = total_train_loss / len(train_loader)

        # ── Validation ──
        model.eval()
        total_val_loss = 0
        with torch.no_grad():
            for batch in val_loader:
                input_ids      = batch["input_ids"].to(device)
                attention_mask = batch["attention_mask"].to(device)
                labels         = batch["labels"].to(device)

                outputs = model(input_ids=input_ids,
                                attention_mask=attention_mask,
                                labels=labels)
                total_val_loss += outputs.loss.item()

        avg_val_loss = total_val_loss / len(val_loader)

        print(f"Epoch {epoch+1}/{EPOCHS} | Train Loss: {avg_train_loss:.4f} | Val Loss: {avg_val_loss:.4f}")

        # Save best model
        if avg_val_loss < best_val_loss:
            best_val_loss = avg_val_loss
            os.makedirs(SAVE_PATH, exist_ok=True)
            model.save_pretrained(SAVE_PATH)
            tokenizer.save_pretrained(SAVE_PATH)
            print(f"  ✅ Best model saved to {SAVE_PATH}")

    print("\nTraining complete!")

if __name__ == "__main__":
    train()