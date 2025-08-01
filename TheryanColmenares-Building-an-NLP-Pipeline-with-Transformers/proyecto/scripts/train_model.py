# train_model.py

import numpy as np
import evaluate
from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    DataCollatorWithPadding,
    TrainingArguments,
    Trainer
)
from huggingface_hub import login

def main():
    # --- 1. Authentication and Data Loading ---
    
    # Log in to Hugging Face Hub to upload the model.
    # You will be asked to paste an access token from your account.
    print("Logging into Hugging Face Hub...")
    login()

    # Load the IMDb dataset.
    print("Loading the IMDb dataset...")
    imdb = load_dataset("imdb")

    # Load the DistilBERT tokenizer. 'uncased' means it's not case-sensitive.
    print("Loading the tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

    # Define the function that will tokenize the text.
    # `truncation=True` cuts texts that exceed the model's maximum length.
    def preprocess_function(examples):
        return tokenizer(examples["text"], truncation=True)

    # Apply tokenization to the entire dataset efficiently.
    print("Tokenizing the dataset...")
    tokenized_imdb = imdb.map(preprocess_function, batched=True)

    # Create a 'data collator' that will dynamically add padding to the data batches.
    # This ensures that all texts in the same batch have the same length.
    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

    # --- 3. Model and Metrics Configuration ---

    # Define label mappings for better interpretation.
    id2label = {0: "NEGATIVE", 1: "POSITIVE"}
    label2id = {"NEGATIVE": 0, "POSITIVE": 1}

    # Load the pre-trained DistilBERT model for sequence classification.
    # `num_labels=2` because we have two classes: positive and negative.
    print("Loading the pre-trained model...")
    model = AutoModelForSequenceClassification.from_pretrained(
        "distilbert-base-uncased",
        num_labels=2,
        id2label=id2label,
        label2id=label2id
    )

    # Load the 'accuracy' metric.
    accuracy_metric = evaluate.load("accuracy")

    # Define the function to calculate metrics during evaluation.
    def compute_metrics(eval_pred):
        predictions, labels = eval_pred
        # `argmax` gets the class with the highest probability.
        predictions = np.argmax(predictions, axis=1)
        return accuracy_metric.compute(predictions=predictions, references=labels)

    # --- 4. Model Training ---

    # Define the training arguments.
    training_args = TrainingArguments(
        output_dir="my_awesome_imdb_model",      # Directory where the model will be saved
        learning_rate=2e-5,                      # Learning rate
        per_device_train_batch_size=16,          # Batch size for training
        per_device_eval_batch_size=16,           # Batch size for evaluation
        num_train_epochs=2,                      # Number of training epochs
        weight_decay=0.01,                       # Weight decay for regularization
        eval_strategy="epoch",
        save_strategy="epoch",                   # Save the model at the end of each epoch
        load_best_model_at_end=True,             # Load the best model at the end of training
        push_to_hub=True,                        # Upload the model to the Hugging Face Hub
        report_to="none",
    )

    # Create the Trainer instance with all the components.
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_imdb["train"],
        eval_dataset=tokenized_imdb["test"],
        tokenizer=tokenizer,
        data_collator=data_collator,
        compute_metrics=compute_metrics,
    )

    # Start the training.
    print("Starting model fine-tuning...")
    trainer.train()

    # Upload the final model to the Hub.
    print("Uploading model to the Hub...")
    trainer.push_to_hub()
    
    print("\nTraining completed and model uploaded to the Hub!")
    print(f"You can find your model at: https://huggingface.co/YOUR_USERNAME/my_awesome_imdb_model")


if __name__ == "__main__":
    main()