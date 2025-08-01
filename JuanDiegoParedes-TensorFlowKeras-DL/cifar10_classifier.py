import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np

# 1. CARGA Y PREPROCESAMIENTO DE CIFAR-10
(x_train, y_train), (x_test, y_test) = datasets.cifar10.load_data()

# Normalizar imágenes a [0, 1]
x_train, x_test = x_train / 255.0, x_test / 255.0

# Convertir etiquetas a un vector plano (de [[3]] a [3])
y_train = y_train.flatten()
y_test = y_test.flatten()

# Lista de nombres de clases para mostrar resultados
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

# 2. DEFINICIÓN DE LA RED NEURONAL CONVOLUCIONAL
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(10, activation='softmax')  # 10 clases
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 3. ENTRENAMIENTO
history = model.fit(x_train, y_train, epochs=10,
                    validation_data=(x_test, y_test))

# 4. EVALUACIÓN
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f'\nPrecisión en conjunto de prueba: {test_acc:.4f}')

# 5. VISUALIZACIÓN DE PREDICCIONES
def plot_sample_predictions(model, x_data, y_true, class_names):
    predictions = model.predict(x_data[:12])
    predicted_labels = np.argmax(predictions, axis=1)

    plt.figure(figsize=(12, 6))
    for i in range(12):
        plt.subplot(3, 4, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(x_data[i])
        color = 'blue' if predicted_labels[i] == y_true[i] else 'red'
        plt.xlabel(f"{class_names[predicted_labels[i]]} ({class_names[y_true[i]]})",
                   color=color)
    plt.tight_layout()
    plt.show()

plot_sample_predictions(model, x_test, y_test, class_names)
