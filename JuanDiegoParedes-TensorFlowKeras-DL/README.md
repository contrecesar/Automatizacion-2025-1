# 🧠 CIFAR-10 Image Classifier with TensorFlow/Keras

This project implements a **Convolutional Neural Network (CNN)** using TensorFlow and Keras to classify images from the **CIFAR-10** dataset. It includes data preprocessing, model training, evaluation, and prediction visualization.

## 🗂️ Project Overview

The CIFAR-10 dataset contains 60,000 color images (32×32 pixels) distributed across 10 classes:

```
['airplane', 'automobile', 'bird', 'cat', 'deer',
 'dog', 'frog', 'horse', 'ship', 'truck']
```

This project demonstrates:
- Data normalization and preprocessing
- Construction of a sequential CNN architecture
- Training with the Adam optimizer
- Evaluation on the test set
- Visualization of model predictions

## 🔧 Technologies

- Python 3.10+
- TensorFlow 2.x
- NumPy
- Matplotlib

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/cifar10-tensorflow.git
cd cifar10-tensorflow
```

### 2. Install Requirements

```bash
pip install tensorflow matplotlib numpy
```

### 3. Run the Classifier

Save the Python script as `cifar10_classifier.py` and execute:

```bash
python cifar10_classifier.py
```

## 🧠 Model Architecture

```text
Input: 32x32 RGB images
↓ Conv2D (32 filters, 3x3, ReLU)
↓ MaxPooling2D (2x2)
↓ Conv2D (64 filters, 3x3, ReLU)
↓ MaxPooling2D (2x2)
↓ Flatten
↓ Dense (128 units, ReLU)
↓ Dropout (30%)
↓ Dense (10 units, Softmax)
```

- Loss function: `sparse_categorical_crossentropy`
- Optimizer: `Adam`
- Metrics: `accuracy`
- Epochs: `10`

## 📊 Evaluation

After training, the model achieves over **80% accuracy** on the CIFAR-10 test set:

```
Test accuracy: ~0.84 (example)
```

## 🖼️ Sample Prediction Visualization

The script includes a function to visualize 12 test images with predicted and actual class labels. Predictions are colored:
- ✅ Blue: Correct
- ❌ Red: Incorrect

## 📎 References

- [TensorFlow Documentation](https://www.tensorflow.org/)
- [CIFAR-10 Dataset](https://www.cs.toronto.edu/~kriz/cifar.html)
- Krizhevsky et al., "ImageNet Classification with Deep Convolutional Neural Networks", NIPS 2012

## 📄 License

This project is open-source under the MIT License.
