import csv, sqlite3

def export_to_csv():
    with sqlite3.connect("store.db") as conn:
        rows = conn.execute("SELECT * FROM products").fetchall()
        with open("products.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "name", "price"])
            writer.writerows(rows)

export_to_csv()