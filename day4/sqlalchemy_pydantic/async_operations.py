import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import User, Base
from schemas import UserSchema, UserCreate
from database import async_engine, AsyncSessionLocal
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Exercise 10: Convert Everything to Async (Using SQLAlchemy 2.0)
async def init_async_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Async database initialized")

async def create_user_async(session: AsyncSession, user: UserCreate) -> UserSchema:
    db_user = User(name=user.name, email=user.email, password=user.password)
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    logger.info(f"Created user async: {db_user.name} with email {db_user.email}")
    return UserSchema.from_orm(db_user)

async def get_users_async(session: AsyncSession, skip: int = 0, limit: int = 100):
    result = await session.execute(
        select(User)
        .filter(User.deleted_at == None)
        .offset(skip)
        .limit(limit)
    )
    users = result.scalars().all()
    return [UserSchema.from_orm(user) for user in users]

async def get_user_by_email_async(session: AsyncSession, email: str):
    result = await session.execute(
        select(User).filter(User.email == email, User.deleted_at == None)
    )
    user = result.scalars().first()
    if not user:
        return None
    return UserSchema.from_orm(user)

async def main():
    await init_async_db()
    
    async with AsyncSessionLocal() as session:
        # Create a new user
        new_user = UserCreate(name="Async User", email="async@example.com", password="password123")
        user = await create_user_async(session, new_user)
        print(f"Created async user: {user}")
        
        # Get all users
        users = await get_users_async(session)
        print(f"Found {len(users)} users")
        
        # Look up a user by email
        found_user = await get_user_by_email_async(session, "async@example.com")
        if found_user:
            print(f"Found user by email: {found_user.name}")

if __name__ == "__main__":
    asyncio.run(main())
