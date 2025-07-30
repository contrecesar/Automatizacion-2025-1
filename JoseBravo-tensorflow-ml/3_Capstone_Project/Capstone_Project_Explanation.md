# Build and train a multivariable regression model to predict housing prices in California using the California Housing Dataset.

step by step:

STEP 1:

import tensorflow as tf

import pandas as pd

from sklearn.datasets import fetch_california_housing

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler
- pandas: often used for data manipulation (not directly used here).
- sklearn: provides access to the dataset and tools for preprocessing and splitting data.


STEP 2:

housing = fetch_california_housing()

X, y = housing.data, housing.target
- X: features such as median income, house age, average rooms, etc.
- y: target variable — the median house price in thousands of dollars.


STEP 3:

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
- Divides the data into training (80%) and testing (20%) sets.
- random_state=42: ensures reproducibility.


STEP 4:

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)
- Applies standardization: centers the data and scales to unit variance.
- Helps the neural network train faster and more reliably.


STEP 5:

model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=[X_train.shape[1]]),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1)
])

Layer breakdown:
- Two hidden layers with 64 neurons each and ReLU activation for non-linear learning.
- The final Dense(1) layer outputs a single continuous value (the predicted price)


STEP 6:

model.compile(optimizer='adam', loss='mse', metrics=['mae'])
- adam: efficient optimizer.
- loss='mse': mean squared error — punishes large errors.
- metrics=['mae']: mean absolute error — more interpretable in dollar terms.


STEP 7:

model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.1)
- Trains for 10 epochs using mini-batches of 32 samples.
- validation_split=0.1: reserves 10% of training data for validation.


STEP 8:

loss, mae = model.evaluate(X_test, y_test)

print(f"Test MAE: {mae:.3f}")
- Evaluates performance on unseen test data.
- Prints the Mean Absolute Error (targeting under 0.5, which implies ~$50K error).
