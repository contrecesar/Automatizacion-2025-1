import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
df = pd.read_csv('data.csv')
print("Primeras filas del DataFrame:")
print(df.head())
df.dropna(inplace=True)

# aca calcular el promedio
promedio = df.groupby('Estado')['Salario'].mean()
print("\nSalario promedio por Estado:")
print(promedio)

# Grafica
promedio.plot(kind='bar', color='skyblue')
plt.title('Salario Promedio por Ciudad')
plt.xlabel('Estado')
plt.ylabel('Salario')
plt.grid(True)
plt.tight_layout()
plt.show()