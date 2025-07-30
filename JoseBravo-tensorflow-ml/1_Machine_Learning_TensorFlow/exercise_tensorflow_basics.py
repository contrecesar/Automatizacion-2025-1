# Objective: Train a simple linear regression model that learns the function Y = 2X using TensorFlow

import tensorflow as tf
import numpy as np

# Input and output data
X = np.array([1.0, 2.0, 3.0, 4.0], dtype=float)
Y = np.array([2.0, 4.0, 6.0, 8.0], dtype=float)

# Model definition: a single dense layer with one neuron
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

# Model compilation
model.compile(optimizer='sgd', loss='mean_squared_error')

# Model training
model.fit(X, Y, epochs=500, verbose=0)

# Testing the model with a new value
result = model.predict(np.array([10.0]))
print(f"Predicción para X=10: {result[0][0]:.2f}")

# Expected result: Approximately 20.0
