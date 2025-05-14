from sqlalchemy.orm import Session
from models import User
from schemas import UserSchema
from database import SessionLocal
from pydantic import BaseModel, EmailStr
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Drill 2: Model Boundary Enforcement

# Pydantic model for profile updates
class UserProfileUpdate(BaseModel):
    name: str = None
    email: EmailStr = None

# Controller layer
class UserController:
    def __init__(self, db: Session):
        self.db = db
    
    def update_user_profile(self, user_id: int, profile_data: UserProfileUpdate) -> UserSchema:
        # Get user from database
        user = self.db.query(User).filter(User.id == user_id, User.deleted_at == None).first()
        if not user:
            raise ValueError(f"User with id {user_id} not found")
        
        # Update user fields if provided
        if profile_data.name:
            user.name = profile_data.name
        if profile_data.email:
            user.email = profile_data.email
            
        # Commit changes
        self.db.commit()
        self.db.refresh(user)
        
        # Convert to Pydantic model before returning
        return UserSchema.from_orm(user)
    
    def get_user(self, user_id: int) -> UserSchema:
        user = self.db.query(User).filter(User.id == user_id, User.deleted_at == None).first()
        if not user:
            return None
        # Never return raw SQLAlchemy model
        return UserSchema.from_orm(user)

if __name__ == "__main__":
    db = SessionLocal()
    controller = UserController(db)
    
    # Get the first user
    first_user = db.query(User).first()
    if first_user:
        # Get user through controller (returning Pydantic model)
        user_data = controller.get_user(first_user.id)
        print(f"User before update: {user_data}")
        
        # Update user profile
        update_data = UserProfileUpdate(name="Updated Name")
        updated_user = controller.update_user_profile(first_user.id, update_data)
        print(f"User after update: {updated_user}")
    else:
        print("No users found in database")
    
    db.close()
