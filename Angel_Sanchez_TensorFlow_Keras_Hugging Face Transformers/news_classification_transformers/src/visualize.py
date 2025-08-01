import os
import json
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import numpy as np

def plot_loss_accuracy(log_dir: str = "models/logs"):
    """
    Plot training loss and evaluation accuracy per epoch from log history.

    Args:
        log_dir (str): Path to the directory containing training logs.
    """
    log_history_path = os.path.join(log_dir, "trainer_state.json")
    if not os.path.exists(log_history_path):
        print("trainer_state.json not found. Skipping loss/accuracy plots.")
        return

    with open(log_history_path, "r") as f:
        log_data = json.load(f)

    history = log_data.get("log_history", [])
    epochs_loss, losses = [], []
    epochs_acc, accs = [], []

    for i, entry in enumerate(history):
        if "loss" in entry:
            losses.append(entry["loss"])
            epochs_loss.append(i + 1)
        if "eval_accuracy" in entry:
            accs.append(entry["eval_accuracy"])
            epochs_acc.append(i + 1)

    if not losses and not accs:
        print("No loss or accuracy data found.")
        return

    plt.figure(figsize=(12, 5))

    # Plot loss
    if losses:
        plt.subplot(1, 2, 1)
        plt.plot(epochs_loss, losses, label="Train Loss", marker="o")
        plt.xlabel("Epoch")
        plt.ylabel("Loss")
        plt.title("Training Loss")
        plt.grid(True)

    # Plot accuracy
    if accs:
        plt.subplot(1, 2, 2)
        plt.plot(epochs_acc, accs, label="Eval Accuracy", color="green", marker="o")
        plt.xlabel("Epoch")
        plt.ylabel("Accuracy")
        plt.title("Evaluation Accuracy")
        plt.grid(True)

    os.makedirs("models/results", exist_ok=True)
    plt.tight_layout()
    plt.savefig("models/results/loss_accuracy.png")
    plt.show()


def plot_confusion_matrix(y_true, y_pred, output_path="models/results/confusion_matrix.png"):
    """
    Plot and save a confusion matrix.

    Args:
        y_true (list): Ground truth labels.
        y_pred (list): Predicted labels.
        output_path (str): Path to save the confusion matrix plot.
    """
    cm = confusion_matrix(y_true, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Fake", "Real"])
    disp.plot(cmap="Blues", values_format="d")
    plt.title("Confusion Matrix")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.show()


if __name__ == "__main__":
    plot_loss_accuracy()
