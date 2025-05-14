from sqlalchemy import create_engine, Column, Integer, Float, ForeignKey, update, select, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from models import Account
from schemas import TransferSchema
from database import SessionLocal
import threading
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Drill 5: Concurrency and Race Condition Management

# Naive implementation - prone to race conditions
def transfer_naive(db: Session, transfer: TransferSchema) -> bool:
    from_account = db.query(Account).filter(Account.id == transfer.from_account_id).first()
    to_account = db.query(Account).filter(Account.id == transfer.to_account_id).first()
    
    if not from_account or not to_account:
        logger.error("One or both accounts not found")
        return False
    
    if from_account.balance < transfer.amount:
        logger.error("Insufficient balance")
        return False
    
    # This is where the race condition can happen
    from_account.balance -= transfer.amount
    to_account.balance += transfer.amount
    
    db.commit()
    logger.info(f"Transferred {transfer.amount} from account {from_account.id} to {to_account.id}")
    return True

# Proper implementation with locking
def transfer_with_locking(db: Session, transfer: TransferSchema) -> bool:
    # Lock both accounts to prevent race conditions
    # Note: In SQLite, this doesn't actually lock but illustrates the concept
    # For real databases, we would use SELECT FOR UPDATE
    try:
        # Lock the accounts in a consistent order to prevent deadlocks
        account_ids = sorted([transfer.from_account_id, transfer.to_account_id])
        
        stmt = text("SELECT * FROM accounts WHERE id = :id FOR UPDATE")
        db.execute(stmt, {"id": account_ids[0]})
        db.execute(stmt, {"id": account_ids[1]})
        
        from_account = db.query(Account).filter(Account.id == transfer.from_account_id).first()
        to_account = db.query(Account).filter(Account.id == transfer.to_account_id).first()
        
        if not from_account or not to_account:
            logger.error("One or both accounts not found")
            return False
        
        if from_account.balance < transfer.amount:
            logger.error("Insufficient balance")
            db.rollback()
            return False
        
        from_account.balance -= transfer.amount
        to_account.balance += transfer.amount
        
        db.commit()
        logger.info(f"Transferred {transfer.amount} from account {from_account.id} to {to_account.id} (with locking)")
        return True
        
    except Exception as e:
        db.rollback()
        logger.error(f"Transfer failed: {str(e)}")
        return False

# Simulate concurrent transfers
def simulate_race_condition():
    # Create accounts if they don't exist
    db = SessionLocal()
    
    account1 = db.query(Account).filter(Account.id == 1).first()
    account2 = db.query(Account).filter(Account.id == 2).first()
    
    if not account1:
        account1 = Account(id=1, user_id=1, balance=1000)
        db.add(account1)
    else:
        account1.balance = 1000
        
    if not account2:
        account2 = Account(id=2, user_id=2, balance=1000)
        db.add(account2)
    else:
        account2.balance = 1000
        
    db.commit()
    db.close()
    
    # Create multiple threads to simulate concurrent transfers
    logger.info("Starting naive transfer simulation (race condition possible)")
    threads = []
    for i in range(5):
        # Each thread tries to transfer $100 from account 1 to account 2
        thread = threading.Thread(
            target=lambda: transfer_naive(SessionLocal(), 
                                        TransferSchema(from_account_id=1, to_account_id=2, amount=100))
        )
        threads.append(thread)
    
    # Start all threads
    for thread in threads:
        thread.start()
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    
    # Check balances
    db = SessionLocal()
    account1 = db.query(Account).filter(Account.id == 1).first()
    account2 = db.query(Account).filter(Account.id == 2).first()
    logger.info(f"Final balances after naive transfers: Account 1: {account1.balance}, Account 2: {account2.balance}")
    db.close()
    
    # Reset balances
    db = SessionLocal()
    account1 = db.query(Account).filter(Account.id == 1).first()
    account2 = db.query(Account).filter(Account.id == 2).first()
    account1.balance = 1000
    account2.balance = 1000
    db.commit()
    db.close()
    
    # Now try with proper locking
    logger.info("Starting transfers with locking")
    threads = []
    for i in range(5):
        thread = threading.Thread(
            target=lambda: transfer_with_locking(SessionLocal(), 
                                               TransferSchema(from_account_id=1, to_account_id=2, amount=100))
        )
        threads.append(thread)
    
    # Start all threads
    for thread in threads:
        thread.start()
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    
    # Check balances
    db = SessionLocal()
    account1 = db.query(Account).filter(Account.id == 1).first()
    account2 = db.query(Account).filter(Account.id == 2).first()
    logger.info(f"Final balances after locked transfers: Account 1: {account1.balance}, Account 2: {account2.balance}")
    db.close()

if __name__ == "__main__":
    simulate_race_condition()
