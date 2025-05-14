import sqlite3

def setup_database():
    """Create necessary tables if they don't exist"""
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    
    # Create products table if not exists
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL
    )
    ''')
    
    # Create inventory log table if not exists
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory_log (
        id INTEGER PRIMARY KEY,
        product_id INTEGER,
        change REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    conn.commit()
    conn.close()

def seed_inventory():
    """Seed the database with sample product data"""
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    
    # Sample products data - without quantity field
    products = [
        (1, "Laptop", 999.99),
        (2, "Smartphone", 699.99),
        (3, "Headphones", 149.99),
        (4, "Monitor", 249.99),
        (5, "Keyboard", 89.99),
        (6, "Mouse", 39.99),
        (7, "External HDD", 119.99),
        (8, "USB Flash Drive", 19.99),
        (9, "Webcam", 69.99),
        (10, "Printer", 199.99)
    ]
    
    # Initial inventory quantities to add to log
    inventory_logs = [
        (1, 10),
        (2, 20),
        (3, 30),
        (4, 15),
        (5, 25),
        (6, 40),
        (7, 18),
        (8, 50),
        (9, 12),
        (10, 8)
    ]
    
    try:
        conn.execute("BEGIN")
        
        # Clear existing data
        cursor.execute("DELETE FROM inventory_log")
        cursor.execute("DELETE FROM products")
        

        cursor.executemany(
            "INSERT INTO products (id, name, price) VALUES (?, ?, ?)", 
            products
        )
        

        cursor.executemany(
            "INSERT INTO inventory_log (product_id, change) VALUES (?, ?)",
            inventory_logs
        )
        
        conn.commit()
        print(f"Database seeded with {len(products)} products")
    except Exception as e:
        conn.rollback()
        print(f"Error seeding database: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    setup_database()
    seed_inventory()