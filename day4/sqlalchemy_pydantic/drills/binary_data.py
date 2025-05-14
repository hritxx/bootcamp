import os
import base64
from sqlalchemy.orm import Session
from models import ProfileImage, User
from database import SessionLocal
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Drill 6: Handling Large Binary Data

# Approach 1: Store images as BLOBs
def store_image_as_blob(db: Session, user_id: int, image_data: bytes) -> ProfileImage:
    # Encode binary data as base64 string for storage
    # In a real app with proper DB support, we'd store raw bytes
    encoded_data = base64.b64encode(image_data).decode('utf-8')
    
    profile_image = ProfileImage(
        user_id=user_id, 
        image_data=encoded_data,
        is_blob=True
    )
    
    db.add(profile_image)
    db.commit()
    db.refresh(profile_image)
    
    logger.info(f"Stored image as BLOB for user {user_id}")
    return profile_image

# Approach 2: Store file paths
def store_image_on_disk(db: Session, user_id: int, image_data: bytes) -> ProfileImage:
    # Create directory if it doesn't exist
    os.makedirs("user_images", exist_ok=True)
    
    # Generate file path
    file_path = f"user_images/user_{user_id}_profile.jpg"
    
    # Save file to disk
    with open(file_path, "wb") as f:
        f.write(image_data)
    
    # Store file path in database
    profile_image = ProfileImage(
        user_id=user_id, 
        image_data=file_path,
        is_blob=False
    )
    
    db.add(profile_image)
    db.commit()
    db.refresh(profile_image)
    
    logger.info(f"Stored image on disk for user {user_id}, path: {file_path}")
    return profile_image

# Compare approaches
def compare_storage_approaches():
    db = SessionLocal()
    
    # Get or create a user
    user = db.query(User).first()
    if not user:
        print("No users found in database")
        return
    
    # Sample image data (just a small placeholder)
    sample_image = b'\x89PNG\r\n\x1a\n' + b'\x00' * 100
    
    # Store using both approaches
    blob_image = store_image_as_blob(db, user.id, sample_image)
    file_image = store_image_on_disk(db, user.id, sample_image)
    
    print("\nPros and Cons of Each Approach:")
    print("\nBLOB Storage:")
    print("✓ Pros:")
    print("  - Atomic operations with the rest of the database")
    print("  - No file system management required")
    print("  - No risk of orphaned files")
    print("  - Simpler backup and restore")
    print("✗ Cons:")
    print("  - Increases database size")
    print("  - Slower performance for large files")
    print("  - Less efficient caching")
    print("  - Can complicate database schema migrations")
    
    print("\nFile System Storage:")
    print("✓ Pros:")
    print("  - Better performance for large files")
    print("  - Doesn't bloat database size")
    print("  - Easier to serve directly (e.g., via nginx)")
    print("  - Can leverage CDNs more easily")
    print("✗ Cons:")
    print("  - Requires synchronization between DB and file system")
    print("  - Risk of orphaned or missing files")
    print("  - More complex backup strategy")
    print("  - File permissions and security concerns")
    
    db.close()

if __name__ == "__main__":
    compare_storage_approaches()
