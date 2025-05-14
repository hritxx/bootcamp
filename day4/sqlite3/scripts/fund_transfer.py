import sqlite3

def transfer_funds(from_id, to_id, amount):
    conn = sqlite3.connect("store.db")
    try:
        conn.execute("BEGIN")
        conn.execute("UPDATE accounts SET balance = balance - ? WHERE account_id = ?", (amount, from_id))
        conn.execute("UPDATE accounts SET balance = balance + ? WHERE account_id = ?", (amount, to_id))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print("Transfer failed:", e)
    finally:
        conn.close()
        

if __name__ == "__main__":
    from_id = int(input("Enter the account ID to transfer from: "))
    to_id = int(input("Enter the account ID to transfer to: "))
    amount = float(input("Enter the amount to transfer: "))
    
    transfer_funds(from_id, to_id, amount)
    print("Transfer completed successfully.")