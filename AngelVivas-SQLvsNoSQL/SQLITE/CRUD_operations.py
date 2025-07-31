from database import create_connection

# ---- CREATE ----
def create_product(conn, product):
    """Inserta un nuevo producto"""
    sql = '''INSERT INTO productos(nombre, precio, stock)
             VALUES(?,?,?)'''
    cursor = conn.cursor()
    cursor.execute(sql, product)
    conn.commit()
    return cursor.lastrowid  # Retorna el ID del nuevo registro

# ---- READ ----
def read_products(conn, filters=None):
    """Consulta productos (con filtros opcionales)"""
    cursor = conn.cursor()
    if filters:
        sql = '''SELECT * FROM productos WHERE stock < ? AND precio > ?'''
        cursor.execute(sql, (filters['max_stock'], filters['min_price']))
    else:
        cursor.execute("SELECT * FROM productos")
    return cursor.fetchall()  # Retorna lista de tuplas

# ---- UPDATE ----
def update_product(conn, product_id, new_price):
    """Actualiza el precio de un producto"""
    sql = '''UPDATE productos SET precio = ? WHERE id = ?'''
    cursor = conn.cursor()
    cursor.execute(sql, (new_price, product_id))
    conn.commit()
    print(f"Producto {product_id} actualizado")

# ---- DELETE ----
def delete_product(conn, product_id):
    """Elimina un producto"""
    sql = '''DELETE FROM productos WHERE id = ?'''
    cursor = conn.cursor()
    cursor.execute(sql, (product_id,))
    conn.commit()
    print(f"Producto {product_id} eliminado")