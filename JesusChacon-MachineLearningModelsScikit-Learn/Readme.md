# 🛍️ RetailX - Customer Churn Analysis

This project demonstrates a machine learning workflow to analyze and predict customer churn for a retail company using Scikit-learn and XGBoost

## 🔍 Overview

The notebook performs the following tasks step-by-step:

1. ✅**Data Loading**
Loads the customer dataset (RetailX_CustomerData.csv) directly from GitHub

2. 📊**Exploratory Data Analysis (EDA)**

   - Displays data structure and descriptive statistics
   - Checks for missing values
   - Visualizes relationships like TotalSpent vs Churn using boxplots and histograms

3. ⚙️**Data Preprocessing**

   - Categorical variables (Region, ProductCategory) are converted to numeric using one-hot encoding
   - Numerical features are standardized for consistent model performance

4. 🔀**Train/Test Split**

The data is split into 70% training and 30% testing using stratified sampling to preserve class balance

5. 🤖**Model Training**

   - The model is trained using XGBoostClassifier with fixed hyperparameters
   - SMOTE is applied to handle class imbalance in the training set
   - The classifier is trained with a custom scale_pos_weight to improve sensitivity to minority class (churned users)

6. 📈 **Model Evaluation**

   - Adjusts classification threshold based on F1-score optimization from the precision-recall curve

   - Prints:

      - Classification report (precision, recall, F1-score, accuracy)
      - ROC AUC score
      - Confusion matrix
      - Plots top 10 important features based on the trained model.

## ▶️ How to Run

You can run the full notebook with one click and no setup required:

👉 [Open in Google Colab](https://colab.research.google.com/github/contrecesar/Automatizacion-2025-1/blob/main/JesusChacon-MachineLearningModelsScikit-Learn/RetailX_Churn_Analysis.ipynb#scrollTo=-S5P3AnbOXxb)

### **Steps:**
Open the notebook in Colab.

Run each cell from top to bottom (Shift + Enter).

The dataset will be downloaded automatically—no upload required.

The model will be trained and evaluated in the same session.

## 📁 Dataset

- **File**: RetailX_CustomerData.csv
- **Source**: Automatically downloaded from GitHub using code in the notebook.

- **Features**:
   - **`CustomerID`**: Unique customer ID
   - **`Region`: **Customer's region
   - **`ProductCategory`:** Primary product category
   - **`TotalSpent`:** Total spending by the customer
   - **`VisitsPerMonth`:** Frequency of visits per month
   - **`LastPurchaseDays`:** Days since last purchase
   - **`Churn`:** Target variable (0 = retained, 1 = churned)
