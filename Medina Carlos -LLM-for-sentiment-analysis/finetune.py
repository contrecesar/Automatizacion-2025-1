from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
from sklearn.metrics import accuracy_score, f1_score
import numpy as np


from datasets import load_dataset


dataset = load_dataset("imdb")


train_dataset = dataset["train"].shuffle(seed=42).select(range(1600))
eval_dataset = dataset["train"].shuffle(seed=42).select(range(1600, 2000))



model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)

def tokenize(batch):
    return tokenizer(batch['text'], truncation=True, padding=True)

encoded_train = train_dataset.map(tokenize, batched=True)
encoded_eval = eval_dataset.map(tokenize, batched=True)


model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)


def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return {
        "accuracy": accuracy_score(labels, predictions),
        "f1": f1_score(labels, predictions)
    }


training_args = TrainingArguments(
    output_dir="./results",
    logging_dir="./logs",
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    num_train_epochs=2,
    use_cpu=True,
)


trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=encoded_train,
    eval_dataset=encoded_eval,
    tokenizer=tokenizer,
    compute_metrics=compute_metrics,
)


trainer.train()


model.save_pretrained("./sentiment-model")
tokenizer.save_pretrained("./sentiment-model")
