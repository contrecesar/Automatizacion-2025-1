import sqlite3
from sqlite3 import Error

def create_connection():
    """Crea una conexión a la base de datos SQLite"""
    conn = None
    try:
        conn = sqlite3.connect('tienda.db')  # Archivo de base de datos
        print("Conexión exitosa a SQLite")
        return conn
    except Error as e:
        print(f"Error al conectar a SQLite: {e}")
    return conn