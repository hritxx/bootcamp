import sqlite3
with open("db/schema.sql") as f:
    conn = sqlite3.connect("store.db")
    conn.executescript(f.read())
    conn.close()