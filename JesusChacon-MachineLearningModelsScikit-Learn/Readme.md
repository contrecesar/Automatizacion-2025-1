# RetailX - Customer Churn Analysis

This project demonstrates a machine learning workflow to analyze and predict customer churn for a retail company using Scikit-learn.

## 🔍 Overview

The notebook performs the following tasks step-by-step:

1. **Data Loading**
   Loads the customer dataset (`RetailX_CustomerData.csv`) directly from GitHub.

2. **Exploratory Data Analysis (EDA)**  
   - Displays data structure and statistics  
   - Checks for missing values  
   - Visualizes relationships like `TotalSpent` vs `Churn`

3. **Data Preprocessing**  
   - Converts categorical variables (`Region`, `ProductCategory`) to numeric using one-hot encoding  
   - Scales numeric features for better model performance

4. **Train/Test Split**  
   Splits the dataset into training and testing sets (70% / 30%).

5. **Model Training**  
   Performs hyperparameter tuning using `GridSearchCV` to train an optimized `RandomForestClassifier` for predicting customer churn.

6. **Model Evaluation**  
   - Prints classification report: precision, recall, F1-score, accuracy  
   - Computes ROC AUC  
   - Visualizes the confusion matrix  
   - Plots top 10 important features

---

## ▶️ How to Run

You can run the full notebook with one click and no setup required:

👉 **[Open in Google Colab](https://colab.research.google.com/github/contrecesar/Automatizacion-2025-1/blob/main/JesusChacon-MachineLearningModelsScikit-Learn/RetailX_Churn_Analysis.ipynb)**

### Steps:
1. Open the notebook using the link above.
2. Execute each cell in order from top to bottom (Shift + Enter).
3. The dataset will be downloaded automatically—no need to upload anything.
4. The model will be trained and evaluated within the same session.

---

## 📁 Dataset

- **File**: `RetailX_CustomerData.csv`
- **Features**:
  - `CustomerID`: Unique customer ID
  - `Region`: Customer's region
  - `ProductCategory`: Main product category
  - `TotalSpent`: Total spending by the customer
  - `VisitsPerMonth`: Monthly visit frequency
  - `LastPurchaseDays`: Days since last purchase
  - `Churn`: Target variable (0 = retained, 1 = churned)

The dataset is automatically downloaded using a code cell in the notebook from this GitHub repository:
