# R Script for Sales Forecasting with Linear Regression in Power BI
# This script is designed to be run within Power Query Editor in Power BI Desktop.
# The input data table from Power BI will be available as a data.frame named 'dataset'.

# --- 1. Install and load necessary libraries ---
# Uncomment the install.packages line if you don't have these libraries installed
# install.packages(c("dplyr", "caret"))
library(dplyr)
library(caret)

# --- 2. Prepare the data (conceptual test data if running outside Power BI for testing) ---
# In Power BI, 'dataset' will already contain your loaded data.
# For local testing, you can uncomment and use the following dummy data:
# dataset <- data.frame(
#   Date = as.Date(c("2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05", "2023-01-06")),
#   Sales = c(100, 110, 105, 120, 115, 130),
#   Advertising_Spend = c(10, 12, 11, 13, 12, 15)
# )

# Ensure the 'Date' column is in Date format if not already
dataset$Date <- as.Date(dataset$Date)

# --- 3. Create and train the Linear Regression model ---
# Define the formula: Dependent_Variable ~ Independent_Variable(s)
model <- lm(Sales ~ Advertising_Spend, data = dataset)

# --- 4. Generate predictions ---
# For forecasting, you would typically have new 'Advertising_Spend' values for future dates.
# For this example, we'll predict on the existing data to show the model's fit.
# If you have future data, you'd load it into a separate data.frame (e.g., 'future_data')
# and then use predict(model, newdata = future_data)
predictions <- predict(model, newdata = dataset)

# --- 5. Add predictions to the original data.frame ---
dataset$Predicted_Sales <- predictions

# --- 6. Select and prepare the output data.frame for Power BI ---
# The final data.frame to be loaded back into Power BI must be named 'output_table'.
# You can select specific columns to return.
output_table <- dataset %>%
  select(Date, Sales, Advertising_Spend, Predicted_Sales)

# Note: Power BI will automatically infer data types.
# Ensure 'output_table' is the last expression in the script for Power Query to pick it up.