import logging
import os
from models import Base
from database import engine

# Initialize logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def init_db():
    Base.metadata.create_all(bind=engine)
    logger.info("Database initialized")

def main():
    logger.info("Starting SQLAlchemy + Pydantic practice exercises")
    
    # Initialize the database
    init_db()
    
    print("\nSQLAlchemy + Pydantic Practice Exercises")
    print("=======================================")
    print("This project contains implementations for all exercises in the following levels:")
    print("1. Beginner Level (Basic CRUD Operations) - See beginner.py")
    print("2. Intermediate Level (Filtering, Updating, Deleting) - See intermediate.py")
    print("3. Advanced Level (Relationships, Transactions, Async) - See advanced.py and async_operations.py")
    print("4. Level-Up Drills - See the drills/ directory")
    print("\nTo run specific exercises, execute the corresponding Python files.")
    print("For example: python beginner.py")

if __name__ == "__main__":
    main()
