import pandas as pd
from sklearn.model_selection import train_test_split
from datasets import Dataset, DatasetDict
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

def load_and_prepare_dataset(real_path: str, fake_path: str):
    """
    Load and prepare the dataset by combining real and fake news files.

    Args:
        real_path (str): Path to the CSV file containing real news.
        fake_path (str): Path to the CSV file containing fake news.

    Returns:
        pd.DataFrame: A combined and shuffled dataframe with 'title' and 'label' columns.
    """
    real_df = pd.read_csv(real_path)
    fake_df = pd.read_csv(fake_path)

    real_df['label'] = 1  # 1 = real news
    fake_df['label'] = 0  # 0 = fake news

    # Combine and shuffle both datasets
    df = pd.concat([real_df, fake_df]).sample(frac=1, random_state=42).reset_index(drop=True)

    # Keep only the relevant columns for classification
    df = df[['title', 'label']]
    return df

def split_dataset(df, test_size=0.2, val_size=0.1):
    """
    Split the dataset into train, validation, and test sets.

    Args:
        df (pd.DataFrame): The dataset to split.
        test_size (float): Proportion of the dataset to use for testing.
        val_size (float): Proportion of the training set to use for validation.

    Returns:
        tuple: Hugging Face Datasets for train, validation, and test.
    """
    # First split off the test set
    train_val_df, test_df = train_test_split(df, test_size=test_size, stratify=df['label'], random_state=42)

    # Then split the remaining into train and validation sets
    train_df, val_df = train_test_split(train_val_df, test_size=val_size, stratify=train_val_df['label'], random_state=42)

    # Convert DataFrames to Hugging Face Datasets
    return Dataset.from_pandas(train_df), Dataset.from_pandas(val_df), Dataset.from_pandas(test_df)

def compute_metrics(pred):
    """
    Compute accuracy, precision, recall and F1 metrics.

    Args:
        pred: Predictions object from the Trainer.

    Returns:
        dict: A dictionary with accuracy, precision, recall, and F1-score.
    """
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    precision, recall, f1, _ = precision_recall_fscore_support(labels, preds, average='binary')
    acc = accuracy_score(labels, preds)
    return {
        'accuracy': acc,
        'precision': precision,
        'recall': recall,
        'f1': f1
    }
