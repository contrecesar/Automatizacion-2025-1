import torch
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
import sys
import os

# Load model and tokenizer
model_dir = os.path.join("models", "final_model")
tokenizer = DistilBertTokenizerFast.from_pretrained(model_dir)
model = DistilBertForSequenceClassification.from_pretrained(model_dir)

# Set device (use GPU if available)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

def predict_text(text):
    """
    Make a prediction for a single text input.

    Args:
        text (str): The news headline or sentence to classify.

    Returns:
        str: "Real" if label is 1, "Fake" if label is 0.
    """
    encoding = tokenizer(text, return_tensors="pt", truncation=True, padding=True).to(device)
    with torch.no_grad():
        outputs = model(**encoding)
        prediction = torch.argmax(outputs.logits, dim=1).item()
    return "Real" if prediction == 1 else "Fake"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python src/predict.py 'Your news headline here'")
    else:
        headline = sys.argv[1]
        label = predict_text(headline)
        print(f"Prediction: {label}")
