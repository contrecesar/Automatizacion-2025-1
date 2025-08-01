# 🧠 MNIST Digit Classifier with Dense Neural Network

This project demonstrates the implementation of a simple yet effective **fully connected neural network** using **TensorFlow** and **Keras**. The model is trained to classify handwritten digits (0–9) from the **MNIST dataset**, a classic benchmark in computer vision and machine learning.

---

## 📊 Project Summary

- **Dataset**: MNIST (70,000 grayscale images of handwritten digits)
- **Model Architecture**:
  - Input: 784 features (flattened 28×28 pixel images)
  - Dense Layer: 128 units with ReLU activation
  - Dense Layer: 64 units with ReLU activation
  - Output Layer: 10 units with Softmax activation
- **Training Configuration**:
  - 10 epochs
  - 20% validation split
  - Optimizer: Adam
- **Test Accuracy**: ~98%
- **Technologies**: Python, TensorFlow, Keras, Matplotlib, Seaborn, scikit-learn

---

## 📂 Outputs

After training, the script generates the following visualizations in the `results/` directory:

- 📈 `accuracy_loss.png`: Accuracy and loss curves over epochs  
- 🔢 `confusion_matrix.png`: Confusion matrix of predictions  
- 🖼️ `predicted_digits.png`: Sample test digits with predicted labels

All plots are saved automatically and also shown on-screen during execution.

---

## 📦 requirements.txt

tensorflow
matplotlib
scikit-learn
numpy
seaborn


---

## 🚀 How to Run (Git Bash on Windows)

Follow the steps below to run the project from scratch:

### 1. Clone the Repository

### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/Scripts/activate  # Use this in Git Bash on Windows
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the Training Script
```bash
python mnist_dense_model.py
```
All generated graphs will be saved in the results/ folder.


