import sqlite3

def update_inventory(product_id, delta):
    conn = sqlite3.connect("store.db")
    try:
        conn.execute("BEGIN")
        conn.execute("UPDATE products SET price = price + ? WHERE id = ?", (delta, product_id))
        conn.execute("INSERT INTO inventory_log (product_id, change) VALUES (?, ?)", (product_id, delta))
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()