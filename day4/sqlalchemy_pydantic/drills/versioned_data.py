from sqlalchemy.orm import Session
from models import User, UserEmailHistory
from schemas import UserSchema, UserEmailHistorySchema
from database import SessionLocal
import logging
from datetime import datetime
from typing import List

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Drill 4: Versioned Data Storage

def update_user_email_with_history(db: Session, user_id: int, new_email: str) -> bool:
    user = db.query(User).filter(User.id == user_id, User.deleted_at == None).first()
    if not user:
        logger.warning(f"User with id {user_id} not found")
        return False
    
    # Store the old email in history
    email_history = UserEmailHistory(
        user_id=user.id,
        email=user.email,
        changed_at=datetime.utcnow()
    )
    db.add(email_history)
    
    # Update the user email
    user.email = new_email
    
    db.commit()
    logger.info(f"Updated email for user {user.name} to {new_email} and stored history")
    return True

def get_email_history(db: Session, user_id: int) -> List[UserEmailHistorySchema]:
    history = db.query(UserEmailHistory)\
        .filter(UserEmailHistory.user_id == user_id)\
        .order_by(UserEmailHistory.changed_at.desc())\
        .all()
    
    return [UserEmailHistorySchema.from_orm(record) for record in history]

if __name__ == "__main__":
    db = SessionLocal()
    
    # Get the first user
    user = db.query(User).first()
    if user:
        print(f"User initial email: {user.email}")
        
        # Update email multiple times to create history
        update_user_email_with_history(db, user.id, "updated1@example.com")
        update_user_email_with_history(db, user.id, "updated2@example.com")
        update_user_email_with_history(db, user.id, "final@example.com")
        
        # Get updated user
        updated_user = db.query(User).filter(User.id == user.id).first()
        print(f"User current email: {updated_user.email}")
        
        # Get email history
        history = get_email_history(db, user.id)
        print(f"Email history (from newest to oldest):")
        for record in history:
            print(f"- {record.email} changed at {record.changed_at}")
    else:
        print("No users found in database")
    
    db.close()
