from database import create_connection
from CRUD_operations import *

def setup_database(conn):
    """Crea la tabla si no existe"""
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER DEFAULT 0
        )
    ''')
    conn.commit()

def main():
    # Conexión a la base de datos
    conn = create_connection()
    if conn is None:
        return

    # Configuración inicial
    setup_database(conn)

    # ---- CREATE ----
    new_product = ('Teclado RGB', 89.99, 15)
    product_id = create_product(conn, new_product)
    print(f"Nuevo producto creado con ID: {product_id}")

    # ---- READ ----
    print("\nTodos los productos:")
    for product in read_products(conn):
        print(product)

    # ---- UPDATE ----
    update_product(conn, product_id, 79.99)  # Actualiza precio

    # ---- READ con filtros ----
    print("\nProductos con stock < 20 y precio > 50:")
    filters = {'max_stock': 20, 'min_price': 50}
    for product in read_products(conn, filters):
        print(product)

    # ---- DELETE ----
    delete_product(conn, product_id)

    # Cerrar conexión
    conn.close()

if __name__ == "__main__":
    main()