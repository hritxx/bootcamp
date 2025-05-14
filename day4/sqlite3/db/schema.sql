CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY, -- SQLite will auto-increment this by default
    name TEXT NOT NULL,
    price REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY ,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS product_categories (
    product_id INTEGER,
    category_id INTEGER,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

CREATE TABLE IF NOT EXISTS accounts (
    account_id INTEGER PRIMARY KEY,
    balance REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS inventory_log (
    id INTEGER PRIMARY KEY ,
    product_id INTEGER,
    change REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);