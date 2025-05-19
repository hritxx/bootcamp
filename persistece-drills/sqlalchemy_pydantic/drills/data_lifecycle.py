from sqlalchemy.orm import Session
from models import Product
from schemas import ProductSchema, ProductCreate
from database import SessionLocal
import logging
from datetime import datetime, timedelta

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Drill 8: Data Lifecycle Management

# Add a product with soft delete capability
def add_product(db: Session, product: ProductCreate) -> Product:
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Soft delete a product
def soft_delete_product(db: Session, product_id: int) -> bool:
    product = db.query(Product).filter(Product.id == product_id, Product.deleted_at == None).first()
    if not product:
        logger.warning(f"Product with id {product_id} not found or already deleted")
        return False
    
    product.deleted_at = datetime.utcnow()
    db.commit()
    logger.info(f"Soft deleted product: {product.name}")
    return True

# Get all active products (not deleted)
def get_active_products(db: Session) -> list[ProductSchema]:
    products = db.query(Product).filter(Product.deleted_at == None).all()
    return [ProductSchema.from_orm(product) for product in products]

# Get all products including deleted
def get_all_products(db: Session) -> list[ProductSchema]:
    products = db.query(Product).all()
    return [ProductSchema.from_orm(product) for product in products]

# Purge old soft-deleted records
def purge_old_records(db: Session, days: int = 30) -> int:
    cutoff_date = datetime.utcnow() - timedelta(days=days)
    
    # Find records to delete
    to_delete = db.query(Product).filter(
        Product.deleted_at != None,
        Product.deleted_at < cutoff_date
    ).all()
    
    count = len(to_delete)
    
    if count > 0:
        # Actually delete the records
        for product in to_delete:
            db.delete(product)
        db.commit()
        logger.info(f"Purged {count} products older than {days} days")
    else:
        logger.info(f"No products found to purge older than {days} days")
    
    return count

if __name__ == "__main__":
    db = SessionLocal()
    
    # Create some products
    products = [
        ProductCreate(name="Product A", description="Description A", price=10.99),
        ProductCreate(name="Product B", description="Description B", price=20.99),
        ProductCreate(name="Product C", description="Description C", price=30.99),
    ]
    
    for p in products:
        add_product(db, p)
    
    # Show all active products
    print("All active products:")
    active_products = get_active_products(db)
    for p in active_products:
        print(f"- {p.name}: ${p.price}")
    
    # Soft delete a product
    if active_products:
        soft_delete_product(db, active_products[0].id)
    
    # Show active products after deletion
    print("\nActive products after deletion:")
    active_products = get_active_products(db)
    for p in active_products:
        print(f"- {p.name}: ${p.price}")
    
    # Show all products including deleted
    print("\nAll products including deleted:")
    all_products = get_all_products(db)
    for p in all_products:
        status = "DELETED" if p.deleted_at else "ACTIVE"
        print(f"- {p.name}: ${p.price} ({status})")
    
    # Simulate purging old records
    print("\nSimulating record purge:")
    # Manually set deleted_at to old date for demonstration
    if all_products and all_products[0].deleted_at:
        product = db.query(Product).filter(Product.id == all_products[0].id).first()
        product.deleted_at = datetime.utcnow() - timedelta(days=31)
        db.commit()
        print(f"Set {product.name} deleted_at to 31 days ago")
    
    # Purge records
    purged = purge_old_records(db)
    print(f"Purged {purged} records")
    
    # Final check
    print("\nRemaining products after purge:")
    all_products = get_all_products(db)
    for p in all_products:
        status = "DELETED" if p.deleted_at else "ACTIVE"
        print(f"- {p.name}: ${p.price} ({status})")
        
    db.close()
