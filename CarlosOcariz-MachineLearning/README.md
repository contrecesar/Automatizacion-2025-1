# Simple-Machine-Learning
IA simple Machine Learning

Iris Classification with K-Nearest Neighbors (KNN) - Code Explanation

This Python script demonstrates a basic machine learning workflow using the Iris flower dataset and the K-Nearest Neighbors (KNN) algorithm.

1. Import Essential Libraries:
   - numpy: For numerical operations
   - datasets: To load built-in datasets
   - train_test_split: For splitting data into training/test sets
   - KNeighborsClassifier: KNN implementation
   - accuracy_score: To evaluate model performance

2. Load the Iris Dataset:
   - A classic dataset with 150 samples of iris flowers
   - 3 species: setosa (0), versicolor (1), virginica (2)
   - 4 features per sample: sepal length/width, petal length/width
   - X: Feature matrix (150x4)
   - y: Target vector (species labels)

3. Explore Data Structure:
   - Print dimensions of feature matrix (150 samples, 4 features)
   - Print unique class labels ([0, 1, 2])

4. Split Data (80% training, 20% testing):
   - Uses train_test_split with random_state=99 for reproducibility
   - Training set: 120 samples (80%)
   - Test set: 30 samples (20%)
   - Stratification is automatic to maintain class proportions

5. Initialize KNN Model:
   - Creates KNeighborsClassifier with n_neighbors=3
   - Uses Euclidean distance by default
   - Will classify based on 3 most similar neighbors

6. Train the Model:
   - Fits the model to training data using .fit()
   - Model learns patterns between features and species

7. Make Predictions:
   - Uses trained model to predict species on test set
   - Generates predictions for all 30 test samples

8. Calculate Accuracy:
   - Compares predictions (y_pred) with true labels (y_test)
   - Computes percentage of correct predictions
   - Example: 96.67% means 29/30 correct

9. Show Prediction Examples:
   - Displays first 5 test samples
   - Compares actual vs predicted species
   - Helps visually verify model performance


Typical Output:
Dimensions of X: (150, 4)
Classes: [0 1 2]
Training samples: 120, Test samples: 30
✅ Model trained!
Model accuracy: 96.67%

Prediction examples:
Actual:    [1 2 0 2 0]
Predicted: [1 2 0 2 0]

Interpretation:
- High accuracy indicates good performance
- First 5 predictions match actual labels
- Model can reliably distinguish iris species
