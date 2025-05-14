from sqlalchemy.orm import Session
from models import User, Base
from schemas import UserCreate, UserSchema
from database import engine, SessionLocal
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Exercise 1: Define a Simple SQLAlchemy Model with Pydantic
def init_db():
    Base.metadata.create_all(bind=engine)
    logger.info("Database initialized")

# Exercise 2: Insert a New User
def create_user(db: Session, user: UserCreate) -> UserSchema:
    db_user = User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    logger.info(f"Created user: {db_user.name} with email {db_user.email}")
    return UserSchema.from_orm(db_user)

# Exercise 3: Fetch Users from the Database
def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[UserSchema]:
    users = db.query(User).filter(User.deleted_at == None).offset(skip).limit(limit).all()
    return [UserSchema.from_orm(user) for user in users]

if __name__ == "__main__":
    init_db()
    db = SessionLocal()
    
    # Create a new user
    new_user = UserCreate(name="John Doe", email="john@example.com", password="password123")
    user = create_user(db, new_user)
    print(f"Created user: {user}")
    
    # Fetch all users
    users = get_users(db)
    print(f"All users: {users}")
    
    db.close()
