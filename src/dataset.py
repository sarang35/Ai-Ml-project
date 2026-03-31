import json
from torch.utils.data import Dataset

class NotesDataset(Dataset):
    def __init__(self, file_path, tokenizer, max_input_len=128, max_target_len=256):
        with open(file_path, "r") as f:
            self.data = json.load(f)

        self.tokenizer = tokenizer
        self.max_input_len = max_input_len
        self.max_target_len = max_target_len

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]

        input_text = f"topic: {item['topic']}\nnotes:"
        target_text = item["notes"]

        input_enc = self.tokenizer(
            input_text,
            max_length=self.max_input_len,
            padding="max_length",
            truncation=True,
            return_tensors="pt"
        )

        target_enc = self.tokenizer(
            target_text,
            max_length=self.max_target_len,
            padding="max_length",
            truncation=True,
            return_tensors="pt"
        )

        labels = target_enc["input_ids"].squeeze()
        # Replace padding token id with -100 so loss ignores padding
        labels[labels == self.tokenizer.pad_token_id] = -100

        return {
            "input_ids": input_enc["input_ids"].squeeze(),
            "attention_mask": input_enc["attention_mask"].squeeze(),
            "labels": labels
        }