# Objective: To build and train a multilayer neural network to classify images of handwritten digits (MNIST)

import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize images to values between 0 and 1
x_train = x_train / 255.0
x_test = x_test / 255.0

# Convert tags to one-hot encoding
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Model definition
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Model compilation
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Model training
model.fit(x_train, y_train, epochs=5, batch_size=32)

# Model evaluation
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Precisión en datos de prueba: {test_acc:.4f}")

# Expected result: Accuracy between 96% and 98%
