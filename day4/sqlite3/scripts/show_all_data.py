import sqlite3
from tabulate import tabulate

def show_all():
    conn = sqlite3.connect("store.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for table_name in tables:
        table = table_name[0]
        print(f"\n--- {table.upper()} ---")
        try:
            cursor.execute(f"PRAGMA table_info({table})")
            columns = [col[1] for col in cursor.fetchall()]
            
            cursor.execute(f"SELECT * FROM {table}")
            rows = cursor.fetchall()
            

            numbered_rows = []
            for i, row in enumerate(rows, 1):
                row_data = [i] + list(row)
                numbered_rows.append(row_data)
            

            headers = ['#'] + columns
            
            # Display using tabulate
            if numbered_rows:
                print(tabulate(numbered_rows, headers=headers, tablefmt="grid"))
            else:
                print("No data in table")
                
        except Exception as e:
            print(f"Error reading {table}: {e}")

    conn.close()

if __name__ == "__main__":
    show_all()