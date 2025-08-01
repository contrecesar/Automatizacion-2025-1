import os
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns

# Create 'results' directory if it doesn't exist
os.makedirs("results", exist_ok=True)

# Load the MNIST dataset (handwritten digits 0–9)
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize pixel values to the range [0, 1]
x_train = x_train / 255.0
x_test = x_test / 255.0

# Flatten 28x28 images into 784-element vectors
x_train = x_train.reshape(-1, 784)
x_test = x_test.reshape(-1, 784)

# Define a fully connected (dense) neural network
model = models.Sequential([
    layers.Dense(128, activation='relu', input_shape=(784,)),  # First hidden layer
    layers.Dense(64, activation='relu'),                       # Second hidden layer
    layers.Dense(10, activation='softmax')                     # Output layer (10 classes)
])

# Compile the model using Adam optimizer and sparse categorical crossentropy loss
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model and save the training history
history = model.fit(x_train, y_train, epochs=10, validation_split=0.2)

# Evaluate the model on the test set
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print(f'\nTest Accuracy: {test_accuracy:.4f}')

# === Plot training and validation accuracy ===
plt.figure(figsize=(10, 5))
plt.plot(history.history['accuracy'], label='Training Accuracy', marker='o')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy', marker='o')
plt.title('Accuracy over Epochs')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True)
plt.savefig("results/accuracy.png")  # Save accuracy plot
plt.close()

# === Plot training and validation loss ===
plt.figure(figsize=(10, 5))
plt.plot(history.history['loss'], label='Training Loss', marker='o')
plt.plot(history.history['val_loss'], label='Validation Loss', marker='o')
plt.title('Loss over Epochs')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)
plt.savefig("results/loss.png")  # Save loss plot
plt.close()

# Predict class probabilities for the test set
y_pred = model.predict(x_test)
y_pred_classes = np.argmax(y_pred, axis=1)

# Print classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred_classes))

# === Plot confusion matrix ===
cm = confusion_matrix(y_test, y_pred_classes)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=[str(i) for i in range(10)],
            yticklabels=[str(i) for i in range(10)])
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.savefig("results/confusion_matrix.png")  # Save confusion matrix plot
plt.close()

# === Display predictions on 5 random test images ===
random_indices = np.random.choice(len(x_test), size=5, replace=False)

for idx, i in enumerate(random_indices):
    image = x_test[i]
    true_label = y_test[i]
    prediction = model.predict(image.reshape(1, 784))
    predicted_label = np.argmax(prediction)

    plt.imshow(image.reshape(28, 28), cmap='gray')
    plt.title(f"True: {true_label} - Predicted: {predicted_label}")
    plt.axis('off')
    plt.savefig(f"results/prediction_{idx+1}.png")  # Save each prediction image
    plt.close()
