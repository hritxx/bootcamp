from sqlalchemy.orm import Session
from models import User
from schemas import UserSchema, UserCreate
from database import SessionLocal
import logging
from datetime import datetime

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Exercise 4: Filter Users Based on Email
def get_user_by_email(db: Session, email: str) -> UserSchema:
    user = db.query(User).filter(User.email == email, User.deleted_at == None).first()
    if not user:
        logger.warning(f"User with email {email} not found")
        return None
    return UserSchema.from_orm(user)

# Exercise 5: Update User Email
def update_user_email(db: Session, user_id: int, new_email: str) -> bool:
    user = db.query(User).filter(User.id == user_id, User.deleted_at == None).first()
    if not user:
        logger.warning(f"User with id {user_id} not found")
        return False
    
    user.email = new_email
    db.commit()
    logger.info(f"Updated email for user {user.name} to {new_email}")
    return True

# Exercise 6: Delete a User
def delete_user(db: Session, user_id: int) -> bool:
    user = db.query(User).filter(User.id == user_id, User.deleted_at == None).first()
    if not user:
        logger.warning(f"User with id {user_id} not found")
        return False
    
    # Soft delete
    user.deleted_at = datetime.utcnow()
    db.commit()
    logger.info(f"Deleted user {user.name}")
    return True

if __name__ == "__main__":
    db = SessionLocal()
    
    # Look up a user by email
    user = get_user_by_email(db, "john@example.com")
    if user:
        print(f"Found user: {user}")
    
    # Update a user's email
    if user:
        success = update_user_email(db, user.id, "john.doe@example.com")
        print(f"Email update successful: {success}")
        
    # Delete a user
    if user:
        success = delete_user(db, user.id)
        print(f"User deletion successful: {success}")
    
    db.close()
