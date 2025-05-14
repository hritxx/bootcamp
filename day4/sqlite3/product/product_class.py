import sqlite3

class Product:
    def __init__(self, db_name='store.db'):
        self.db_name = db_name

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def add_product(self, name, price):
        if not isinstance(name, str) or not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Invalid name or price")

        try:
            with self._connect() as conn:
                conn.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
        except sqlite3.Error as e:
            print("DB Error:", e)

    def update_price(self, prod_id, new_price):
        try:
            with self._connect() as conn:
                conn.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, prod_id))
        except sqlite3.Error as e:
            print("Error updating:", e)

    def delete_product(self, prod_id):
        try:
            with self._connect() as conn:
                conn.execute("DELETE FROM products WHERE id = ?", (prod_id,))
        except sqlite3.Error as e:
            print("Error deleting:", e)

    def list_all(self):
        with self._connect() as conn:
            for row in conn.execute("SELECT * FROM products"):
                print(row)

    def search_by_name(self, fragment):
        with self._connect() as conn:
            rows = conn.execute("SELECT * FROM products WHERE name LIKE ?", (f'%{fragment}%',)).fetchall()
            return rows