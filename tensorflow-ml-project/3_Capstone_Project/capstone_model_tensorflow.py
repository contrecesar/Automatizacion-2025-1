# Objective: Build a multivariate regression model with TensorFlow to predict housing prices in California

import tensorflow as tf
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the dataset
housing = fetch_california_housing()
X, y = housing.data, housing.target

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model definition
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=[X_train.shape[1]]),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1)
])

# Model compilation
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Training
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.1)

# Assessment
loss, mae = model.evaluate(X_test, y_test)
print(f"Error absoluto medio en test: {mae:.3f}")

# Expected result: MAE < 0.5 (approximately $50,000 error)
