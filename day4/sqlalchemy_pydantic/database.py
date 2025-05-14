from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

# SQLite Database
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# PostgreSQL Async Database
ASYNC_SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost/asyncdb"
async_engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL)
AsyncSessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=async_engine,
    class_=AsyncSession
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_async_db():
    async with AsyncSessionLocal() as session:
        yield session
