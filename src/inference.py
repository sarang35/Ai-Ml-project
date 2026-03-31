import os
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(SCRIPT_DIR, "..", "model")

def generate_notes(topic: str, model, tokenizer, device) -> str:
    input_text = f"topic: {topic}\nnotes:"
    inputs = tokenizer(
        input_text,
        return_tensors="pt",
        max_length=128,
        truncation=True,
        padding="longest"
    ).to(device)

    with torch.no_grad():
        output_ids = model.generate(
            inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_new_tokens=150,
            num_beams=5,
            no_repeat_ngram_size=3,
            early_stopping=True,
            length_penalty=0.8
        )

    return tokenizer.decode(output_ids[0], skip_special_tokens=True)


def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Loading model...\n")

    tokenizer = T5Tokenizer.from_pretrained(MODEL_PATH)
    model = T5ForConditionalGeneration.from_pretrained(MODEL_PATH).to(device)
    model.eval()

    print("=== Note Making AI ===")
    print("Type a topic and get notes. Type 'quit' to exit.\n")

    while True:
        topic = input("Enter topic: ").strip()
        if topic.lower() == "quit":
            break
        if not topic:
            continue

        notes = generate_notes(topic, model, tokenizer, device)
        print(f"\n📝 Notes for '{topic}':\n{notes}\n{'='*50}\n")

if __name__ == "__main__":
    main()