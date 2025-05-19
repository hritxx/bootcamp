from sqlalchemy import create_engine, Column, Integer, String, DateTime, MetaData, Table
from sqlalchemy.sql import text
from datetime import datetime
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Drill 1: Schema Evolution and Migrations
def execute_schema_migration():
    # Initial schema with just id and name
    engine = create_engine("sqlite:///./migration_example.db")
    
    # Create initial schema
    metadata = MetaData()
    users_table = Table(
        "users", 
        metadata,
        Column("id", Integer, primary_key=True),
        Column("name", String(50))
    )
    
    # Create initial table
    metadata.create_all(engine)
    logger.info("Created initial users table with id and name")
    
    # Insert some sample data
    with engine.connect() as conn:
        conn.execute(text("INSERT INTO users (name) VALUES ('John'), ('Jane')"))
        conn.commit()
    
    logger.info("Inserted sample data")
    
    # Migration SQL for adding created_at column with default
    migration_sql = """
    -- Migration script to add created_at column
    ALTER TABLE users ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;
    
    -- Update existing records to have a created_at value
    UPDATE users SET created_at = CURRENT_TIMESTAMP WHERE created_at IS NULL;
    """
    
    # Execute migration
    with engine.connect() as conn:
        conn.execute(text(migration_sql))
        conn.commit()
    
    logger.info("Migration executed: added created_at column")
    
    # Verify migration
    with engine.connect() as conn:
        result = conn.execute(text("PRAGMA table_info(users)")).all()
        for col in result:
            print(f"Column: {col}")
        
        users = conn.execute(text("SELECT * FROM users")).all()
        for user in users:
            print(f"User: {user}")

if __name__ == "__main__":
    execute_schema_migration()
