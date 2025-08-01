import torch
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset
from src.utils import load_and_prepare_dataset, split_dataset, compute_metrics
from src.visualize import plot_confusion_matrix
import numpy as np

# Load and prepare dataset
df = load_and_prepare_dataset("data/True.csv", "data/Fake.csv")
_, _, test_dataset = split_dataset(df)

# Load tokenizer and tokenize test set
tokenizer = DistilBertTokenizerFast.from_pretrained("models/final_model")

def tokenize_function(examples):
    return tokenizer(examples["title"], truncation=True, padding="max_length")

test_dataset = test_dataset.map(tokenize_function, batched=True)
test_dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "label"])

# Load trained model
model = DistilBertForSequenceClassification.from_pretrained("models/final_model")

# Setup dummy TrainingArguments (just for evaluation)
training_args = TrainingArguments(
    output_dir="models/results",
    per_device_eval_batch_size=32,
    do_eval=True,
    report_to="none"
)

# Use Trainer for prediction
trainer = Trainer(
    model=model,
    args=training_args,
    tokenizer=tokenizer
)

# Predict
predictions = trainer.predict(test_dataset)
y_pred = np.argmax(predictions.predictions, axis=1)
y_true = predictions.label_ids

# Plot confusion matrix
plot_confusion_matrix(y_true, y_pred, output_path="models/results/confusion_matrix.png")
print(" Confusion matrix saved to models/results/confusion_matrix.png")
