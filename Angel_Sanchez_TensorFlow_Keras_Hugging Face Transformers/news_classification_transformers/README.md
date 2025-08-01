# 📰 News Classification with Transformers

This project implements a binary news classifier using Hugging Face Transformers and the DistilBERT model. The goal is to detect whether a news headline is **real** or **fake**, using a fine-tuned transformer model trained on labeled news headlines.

---

## 📥 Dataset

Download the dataset from Kaggle:  
🔗 [Fake and Real News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset/data)

Place the following two CSV files into the `data/` folder of the project:

- `True.csv` – headlines of real news articles  
- `Fake.csv` – headlines of fake news articles  

---

## ⚙️ Installation and Setup

Make sure you have Python 3.8+ and Git Bash or a Unix-like terminal available.

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name/news_classification_transformers

# 2. Create and activate virtual environment
python -m venv venv
source venv/Scripts/activate  # On Windows Git Bash

# 3. Install required packages
pip install -r requirements.txt
```
##🚀 Running the Project

1. Fine-tune the model on the dataset:

```bash
python src/main.py
  #if it doesn't work use
python -m src.main.py
```
This will tokenize the dataset, split it into train/validation/test sets, fine-tune the distilbert-base-uncased model, and save the model in models/final_model/.

2. View training results:
Accuracy and loss graphs will be saved in models/results/loss_accuracy.png.

A confusion matrix image will be saved in models/results/confusion_matrix.png.

To regenerate the confusion matrix:

```bash
python src/confusion.py
 #if it doesn't work use
python -m src.confusion.py

```
3. Predict new headlines:
You can predict whether a headline is real or fake with:

```bash
python src/predict.py "(Any news headline)"
```
