from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from models import User, Post, Base
from schemas import UserSchema, UserCreate, PostCreate, UserWithPosts
from database import engine, SessionLocal
import logging
from typing import List

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Exercise 7: Add a Post Table and Create a Relationship
def init_db():
    Base.metadata.create_all(bind=engine)
    logger.info("Database initialized with Post table")

# Create a post for a user
def create_user_post(db: Session, post: PostCreate, user_id: int):
    db_post = Post(**post.dict(), user_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

# Exercise 8: Fetch a User and Their Posts
def get_user_with_posts(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id, User.deleted_at == None).first()
    if not user:
        return None
    return UserWithPosts.from_orm(user)

# Exercise 9: Use Transactions for Bulk Inserts
def bulk_insert_users(db: Session, users: List[UserCreate]) -> List[UserSchema]:
    created_users = []
    
    try:
        for user_data in users:
            db_user = User(name=user_data.name, email=user_data.email, password=user_data.password)
            db.add(db_user)
        
        db.commit()
        
        # Fetch the newly created users
        emails = [user.email for user in users]
        created_db_users = db.query(User).filter(User.email.in_(emails)).all()
        created_users = [UserSchema.from_orm(user) for user in created_db_users]
        
    except SQLAlchemyError as e:
        logger.error(f"Error during bulk insert: {str(e)}")
        db.rollback()
        raise
        
    return created_users

if __name__ == "__main__":
    init_db()
    db = SessionLocal()
    
    # Create a user if none exists
    existing_user = db.query(User).first()
    if not existing_user:
        new_user = UserCreate(name="Jane Doe", email="jane@example.com", password="password123")
        existing_user = User(name=new_user.name, email=new_user.email, password=new_user.password)
        db.add(existing_user)
        db.commit()
        db.refresh(existing_user)
    
    # Create posts for the user
    post1 = PostCreate(title="First Post", content="This is my first post!")
    post2 = PostCreate(title="Second Post", content="This is my second post!")
    
    create_user_post(db, post1, existing_user.id)
    create_user_post(db, post2, existing_user.id)
    
    # Fetch the user with posts
    user_with_posts = get_user_with_posts(db, existing_user.id)
    if user_with_posts:
        print(f"User: {user_with_posts.name}")
        for post in user_with_posts.posts:
            print(f"- Post: {post.title}")
    
    # Bulk insert users
    bulk_users = [
        UserCreate(name="User 1", email="user1@example.com", password="password123"),
        UserCreate(name="User 2", email="user2@example.com", password="password123"),
        UserCreate(name="User 3", email="user3@example.com", password="password123"),
    ]
    
    try:
        created_users = bulk_insert_users(db, bulk_users)
        print(f"Created {len(created_users)} users in bulk")
    except Exception as e:
        print(f"Failed to create users: {str(e)}")
    
    db.close()
