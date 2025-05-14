import sqlite3

def fetch_products_with_categories():
    with sqlite3.connect("store.db") as conn:
        query = """
        SELECT p.name, c.name
        FROM products p
        JOIN product_categories pc ON p.id = pc.product_id
        JOIN categories c ON pc.category_id = c.id;
        """
        return conn.execute(query).fetchall()

def total_inventory_value():
    with sqlite3.connect("store.db") as conn:
        return conn.execute("SELECT SUM(price) FROM products").fetchone()[0]