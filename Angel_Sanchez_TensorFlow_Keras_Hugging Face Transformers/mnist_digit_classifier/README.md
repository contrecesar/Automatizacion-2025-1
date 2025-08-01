# MNIST Digit Classifier with Dense Neural Network

This project demonstrates a simple but effective implementation of a fully connected (dense) neural network using TensorFlow and Keras. The model is trained to classify handwritten digits (0–9) from the popular MNIST dataset.

## 📊 Project Summary

- **Dataset:** MNIST (70,000 grayscale images of handwritten digits)
- **Model Architecture:**
  - Input layer: 784 features (flattened 28x28 pixels)
  - Dense layer with 128 ReLU units
  - Dense layer with 64 ReLU units
  - Output layer with 10 softmax units
- **Training:** 10 epochs with 20% validation split
- **Test Accuracy:** ~98%
- **Tools Used:** Python, TensorFlow, Keras, Matplotlib, scikit-learn

## 🧪 Example Output

At the end of the training, the model achieves a test accuracy of **97.55%** and generates a classification report like the one below:


Additionally, the script displays 5 randomly selected test images and their predicted labels:

![Digit Predictions](example_output.png)

## 📦 requirements.txt


tensorflow
matplotlib
scikit-learn

##🚀 How to Run

python -m venv venv
source venv/bin/activate  # On Windows use: .\venv\Scripts\activate


pip install -r requirements.txt

python mnist_dense_model.py

