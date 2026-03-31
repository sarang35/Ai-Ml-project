# 📝 Note Making AI

A fine-tuned T5 model that generates structured, bullet-point notes from any topic or prompt. Built with PyTorch and Hugging Face Transformers.

---

## 🚀 Features

- Generate organized notes from any topic in seconds
- Fine-tuned on a custom topic → notes dataset
- Beam search decoding for higher quality output
- ROUGE-based evaluation built in
- Runs on CPU or GPU automatically

---

## 🗂️ Project Structure

```
note-making-ai/
├── data/
│   ├──generate_large_dataset.py
│   └── notes_dataset.json      # Training data (topic → notes pairs)
├── src/
│   ├── dataset.py              # PyTorch Dataset class
│   ├── train.py                # Training loop with validation
│   ├── evaluate.py             # ROUGE score evaluation
│   └── inference.py            # Interactive CLI to use the model
├── model/                      # Saved model after training (auto-created)
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/note-making-ai.git
cd note-making-ai
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

**Requirements:**
- transformers==4.40.0
- datasets==2.19.0
- torch==2.2.2
- sentencepiece==0.2.0
- scikit-learn==1.4.2
- rouge-score==0.1.2
- accelerate==0.29.3

---

## 📦 Dataset Format

Add your training data to `data/notes_dataset.json` as a  list of topic → notes pairs:

```json
[
  {
    "topic": "Photosynthesis",
    "notes": "- Process by which plants make food using sunlight\n- Takes place in chloroplasts\n- Equation: CO2 + H2O + light → glucose + O2"
  },
  {
    "topic": "Newton's Laws of Motion",
    "notes": "- First law: Object stays at rest unless acted upon\n- Second law: F = ma\n- Third law: Every action has an equal and opposite reaction"
  }
]
```

> 💡 Tip: Aim for at least **100–500 pairs** for good results. More data = better notes.

---

## 🏋️ Training

```bash
cd src
python train.py
```

Key config options inside `train.py`:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `MODEL_NAME` | `t5-small` | Base model (`t5-small` or `t5-base`) |
| `EPOCHS` | `10` | Number of training epochs |
| `BATCH_SIZE` | `4` | Training batch size |
| `LR` | `5e-4` | Learning rate |
| `VAL_SPLIT` | `0.1` | Fraction of data used for validation |

The best model is automatically saved to the `model/` folder.

---

## 📊 Evaluation

```bash
python evaluate.py
```

Prints per-sample predictions vs references, and average **ROUGE-1, ROUGE-2, and ROUGE-L** scores across the first 10 samples.

Example output:
```
Topic     : Photosynthesis
Generated : - Plants use sunlight to produce food
            - Occurs in chloroplasts
            - CO2 + H2O + light → glucose + O2
ROUGE-L   : 0.712
```

---

## 🤖 Inference (Use the Model)

```bash
python inference.py
```

Interactive CLI — just type any topic:

```
=== Note Making AI ===
Enter topic: Black Holes

📝 Notes for 'Black Holes':
- Regions of space where gravity is so strong light cannot escape
- Formed from collapsed massive stars
- Defined by the event horizon — the point of no return
- Studied using gravitational waves and X-ray observations
==================================================
```

Type `quit` to exit.

---

## 🔁 Full Workflow

```
1. Prepare data   →  data/notes_dataset.json
2. Train          →  python src/train.py
3. Evaluate       →  python src/evaluate.py
4. Use it         →  python src/inference.py
```

---

## 💡 Tips & Troubleshooting

| Issue | Fix |
|-------|-----|
| Training is slow | Use Google Colab (free GPU) or switch to `t5-small` |
| Low ROUGE scores | Add more training data or increase epochs |
| Repetitive output | Increase `no_repeat_ngram_size` in `inference.py` |
| Out of memory | Reduce `BATCH_SIZE` to 2 or 1 |
| Want better quality | Change `t5-small` → `t5-base` in `train.py` |

---

## 🧠 Model Info

| Property | Value |
|----------|-------|
| Base Model | Google T5 (Text-to-Text Transfer Transformer) |
| Task | Conditional text generation |
| Decoding | Beam search (num_beams=4) |
| Framework | PyTorch + Hugging Face Transformers |

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 🙌 Acknowledgements

- [Hugging Face Transformers](https://github.com/huggingface/transformers)
- [Google T5 Paper](https://arxiv.org/abs/1910.10683)
- [PyTorch](https://pytorch.org/)
