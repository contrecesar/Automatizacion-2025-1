RetailX Customer Churn Analysis
This project demonstrates a machine learning workflow to analyze and predict customer churn for a retail company using Scikit-learn.

Overview
The notebook performs the following tasks step-by-step:

Data Loading: Load the customer dataset containing features such as spending, visits, region, and churn status.

Exploratory Data Analysis (EDA): Explore dataset structure, check for missing values, and visualize key relationships like spending vs churn.

Data Preprocessing: Convert categorical variables to numeric using one-hot encoding and scale the features for model training.

Train/Test Split: Split the dataset into training and testing subsets.

Model Training: Train a Random Forest classifier to predict whether a customer will churn or not.

Model Evaluation: Evaluate the model using classification metrics (precision, recall, F1-score, accuracy, ROC AUC) and visualize results with confusion matrix and feature importance plots.

How to Run
Simply open the notebook in Google Colab and run each cell sequentially:

RetailX Churn Analysis Notebook

Requirements
All necessary Python libraries (pandas, numpy, seaborn, matplotlib, scikit-learn) are pre-installed in Colab. No additional setup is needed.

Notes
The dataset RetailX_CustomerData.csv is automatically downloaded from the GitHub repository when running the notebook.

Execute the cells in order to ensure data is properly loaded, processed, and the model is trained and evaluated.

If you have any questions or suggestions, feel free to reach out!
