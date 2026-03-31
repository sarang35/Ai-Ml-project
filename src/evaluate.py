import os
import torch
import json
from rouge_score import rouge_scorer
from transformers import T5ForConditionalGeneration, T5Tokenizer
from dataset import NotesDataset

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(SCRIPT_DIR, "..", "model")
DATA_PATH = os.path.join(SCRIPT_DIR, "..", "data", "notes_dataset.json")


def load_model_and_tokenizer(device):
    tokenizer = T5Tokenizer.from_pretrained(MODEL_PATH)
    model = T5ForConditionalGeneration.from_pretrained(MODEL_PATH).to(device)
    model.eval()
    return model, tokenizer


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

    return tokenizer.decode(output_ids[0], skip_special_tokens=True).strip()


def evaluate(num_samples: int = 20):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Evaluating on device: {device}\n")

    model, tokenizer = load_model_and_tokenizer(device)
    dataset = NotesDataset(DATA_PATH, tokenizer, max_input_len=128, max_target_len=256)

    scorer = rouge_scorer.RougeScorer(["rouge1", "rouge2", "rougeL"], use_stemmer=True)
    total_scores = {"rouge1": 0.0, "rouge2": 0.0, "rougeL": 0.0}

    num_samples = min(num_samples, len(dataset))
    print(f"Using {num_samples} samples from {len(dataset)} total examples.\n")

    for index in range(num_samples):
        item = dataset.data[index]
        predicted = generate_notes(item["topic"], model, tokenizer, device)
        reference = item["notes"].strip()

        scores = scorer.score(reference, predicted)
        for key in total_scores:
            total_scores[key] += scores[key].fmeasure

        if index < 5:
            print(f"Topic     : {item['topic']}")
            print(f"Predicted : {predicted}\n")
            print(f"Reference : {reference}\n")
            print("-" * 60)

    avg_scores = {key: total_scores[key] / num_samples for key in total_scores}
    print("\nAverage ROUGE scores:")
    for key, value in avg_scores.items():
        print(f"{key}: {value:.4f}")


if __name__ == "__main__":
    evaluate(20)
