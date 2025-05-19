import sqlite3

def batch_insert(products):
    try:
        with sqlite3.connect("store.db") as conn:
            conn.executemany("INSERT INTO products (name, price) VALUES (?, ?)", products)
    except Exception as e:
        print("Batch insert failed:", e)

batch_insert([("Shampoo", 120.5), ("Toothpaste", 45.0)])