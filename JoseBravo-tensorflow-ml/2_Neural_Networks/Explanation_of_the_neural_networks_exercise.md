# Build and train a multi-layer neural network to classify handwritten digit images using the MNIST dataset.

step by step:

STEP 1:

import tensorflow as tf

from tensorflow.keras.datasets import mnist

from tensorflow.keras.utils import to_categorical

- mnist: built-in dataset of handwritten digits (0–9).
- to_categorical: converts integer labels into one-hot encoded vectors.


STEP 2:

(x_train, y_train), (x_test, y_test) = mnist.load_data()
- Downloads and loads the dataset.
- x_train: images used for training (60,000 examples).
- x_test: images for evaluation (10,000 examples).
- Each image is 28×28 pixels in grayscale.


STEP 3:

x_train = x_train / 255.0

x_test = x_test / 255.0
- Pixel values range from 0 to 255.
- Dividing by 255 scales them to 0–1, which helps the model learn more efficiently.


STEP 4:

y_train = to_categorical(y_train, 10)

y_test = to_categorical(y_test, 10)
- Converts integer labels (e.g. 7) into one-hot vectors (e.g. [0,0,0,0,0,0,0,1,0,0]).
- There are 10 classes (digits 0 through 9).


STEP 5:

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

Layer breakdown:
- Flatten: turns each 28×28 image into a 784-element vector.
- Dense(128): first hidden layer with 128 neurons and ReLU activation.
- Dense(64): second hidden layer with 64 neurons, also with ReLU.
- Dense(10): output layer with 10 neurons and softmax to give class probabilities.

STEP 6:

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
- adam: a fast and efficient optimizer.
- categorical_crossentropy: loss function suitable for multi-class classification.
- accuracy: metric to track during training and evaluation.

STEP 7:

model.fit(x_train, y_train, epochs=5, batch_size=32)
- Trains for 5 full passes (epochs) over the training data.
- batch_size=32: processes 32 images at a time before updating weights.


STEP 8:

test_loss, test_acc = model.evaluate(x_test, y_test)

print(f"Precisión en datos de prueba: {test_acc:.4f}")
- Evaluates performance on unseen test data.
- Prints the accuracy (expected: between 96% and 98%).
