import pandas as pd
from transformers import (
    DistilBertTokenizerFast,
    DistilBertForSequenceClassification,
    Trainer,
    TrainingArguments,
    DataCollatorWithPadding,
)
from datasets import Dataset
from src.utils import load_and_prepare_dataset, split_dataset, compute_metrics
import torch
import os
import json

import transformers
print("Transformers version:", transformers.__version__)
# Load and prepare dataset
df = load_and_prepare_dataset("data/True.csv", "data/Fake.csv")
train_dataset, val_dataset, test_dataset = split_dataset(df)

# Load tokenizer
tokenizer = DistilBertTokenizerFast.from_pretrained("distilbert-base-uncased")

# Tokenize datasets
def tokenize_function(examples):
    return tokenizer(examples["title"], truncation=True)

train_dataset = train_dataset.map(tokenize_function, batched=True)
val_dataset = val_dataset.map(tokenize_function, batched=True)
test_dataset = test_dataset.map(tokenize_function, batched=True)

# Load model
model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=2)

# Prepare data collator to pad dynamically
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

# Define training arguments
training_args = TrainingArguments(
    output_dir="models/results",
    eval_strategy="epoch",  
    save_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_dir="models/logs",
    logging_steps=10,
    load_best_model_at_end=True,
    metric_for_best_model="accuracy",
    logging_strategy="epoch", 
)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    tokenizer=tokenizer,
    data_collator=data_collator, 
    compute_metrics=compute_metrics,
)

# Train and evaluate
trainer.train()
trainer.evaluate()

# Manual log verification and saving
trainer_state = {
    "log_history": trainer.state.log_history
}
os.makedirs("models/logs", exist_ok=True)
with open("models/logs/trainer_state.json", "w") as f:
    import json
    json.dump(trainer_state, f, indent=2)

# Save model and tokenizer
model.save_pretrained("models/final_model")
tokenizer.save_pretrained("models/final_model")
