# IMDb Sentiment Analysis with DistilBERT

This project is a complete and verifiable demonstration of fine-tuning a `DistilBERT` model for binary sentiment analysis. It uses the IMDb movie review dataset and the Hugging Face ecosystem to train a model capable of classifying text as either **POSITIVE** or **NEGATIVE**.

## Features

* Fine-tunes `distilbert-base-uncased` for a text classification task.
* Uses the standard IMDb dataset for training and evaluation.
* Includes separate scripts for training (`train_model.py`) and inference (`use_model.py`).
* Pushes the final trained model to the Hugging Face Hub for easy access and deployment.
* Features an interactive inference script that allows for real-time testing with user input.

## Model

The final fine-tuned model is available on the Hugging Face Hub and can be used directly for inference tasks.

* **Model Link:** [ther04/my_awesome_imdb_model](https://huggingface.co/ther04/my_awesome_imdb_model)

## Installation

To set up the project locally, please follow these steps.

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-name>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Log in to Hugging Face:**
    You'll need to authenticate with your Hugging Face account to push the model to the Hub. It's recommended to use a token with `write` permissions.
    ```bash
    huggingface-cli login
    ```

## Usage

The project is split into two main parts: training and inference.

### Training

To fine-tune the model from scratch, run the training script. This will perform all the steps: data loading, preprocessing, training, and uploading the final model to the Hugging Face Hub.

```bash
python scripts/train_model.py