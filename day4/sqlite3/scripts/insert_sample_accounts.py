import sqlite3

with sqlite3.connect("store.db") as conn:
    conn.execute("INSERT INTO accounts (account_id, balance) VALUES (1, 1000), (2, 500)")