# Python Script for Sales Forecasting with Linear Regression in Power BI
# This script is designed to be run within Power Query Editor in Power BI Desktop.
# The input data table from Power BI will be available as a pandas DataFrame named 'dataset'.

# --- 1. Import necessary libraries ---
import pandas as pd
from sklearn.linear_model import LinearRegression
import io

# --- 2. Prepare the data (conceptual test data if running outside Power BI for testing) ---
# In Power BI, 'dataset' will already contain your loaded data.
# For local testing, you can uncomment and use the following dummy data:
# data = """Date,Sales,Advertising_Spend
# 2023-01-01,100,10
# 2023-01-02,110,12
# 2023-01-03,105,11
# 2023-01-04,120,13
# 2023-01-05,115,12
# 2023-01-06,130,15
# """
# dataset = pd.read_csv(io.StringIO(data), parse_dates=['Date'])

# Ensure the 'Date' column is in datetime format if not already
dataset['Date'] = pd.to_datetime(dataset['Date'])

# --- 3. Define independent (X) and dependent (y) variables ---
# Make sure these column names match your Power BI data table
X = dataset[['Advertising_Spend']] # Independent variable(s) - must be a DataFrame
y = dataset['Sales']             # Dependent variable - must be a Series

# --- 4. Create and train the Linear Regression model ---
model = LinearRegression()
model.fit(X, y)

# --- 5. Generate predictions ---
# For forecasting, you would typically have new 'Advertising_Spend' values for future dates.
# For this example, we'll predict on the existing data to show the model's fit.
# If you have future data, you'd load it into a separate DataFrame (e.g., 'future_data')
# and then use model.predict(future_data[['Advertising_Spend']])
predictions = model.predict(X)

# --- 6. Add predictions to the original DataFrame ---
dataset['Predicted_Sales'] = predictions

# --- 7. Select and prepare the output DataFrame for Power BI ---
# The final DataFrame to be loaded back into Power BI must be named 'output_table'.
# You can select specific columns to return.
output_table = dataset[['Date', 'Sales', 'Advertising_Spend', 'Predicted_Sales']]

# Note: Power BI will automatically infer data types.
# Ensure 'output_table' is the last expression in the script for Power Query to pick it up.
