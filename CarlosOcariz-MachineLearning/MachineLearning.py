# Import essential libraries
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score 

# Load Iris dataset (included in Scikit-Learn)
iris = datasets.load_iris()
X = iris.data  # Features: sepal/petal length/width
y = iris.target  # Target variable: species (0, 1, 2)

# Explore structure
print("Dimensions of X:", X.shape)  # (150 samples, 4 features)
print("Classes:", np.unique(y))  # [0, 1, 2] → 3 species

# 80% training, 20% testing (random seed=99 for reproducibility)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=99)
print(f"Training samples: {X_train.shape[0]}, Test samples: {X_test.shape[0]}")

# Initialize KNN model (k-nearest neighbors)
knn_model = KNeighborsClassifier(n_neighbors=3)  # Use 3 neighbors

# Train with training data
knn_model.fit(X_train, y_train)
print("✅ Model trained!")

# Predict on test data
y_pred = knn_model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy:.2%}")  # E.g.: 96.67%

# Show predictions vs actual values
print("\nPrediction examples:")
print("Actual:   ", y_test[:5])    # True values
print("Predicted:", y_pred[:5])    # Predictions