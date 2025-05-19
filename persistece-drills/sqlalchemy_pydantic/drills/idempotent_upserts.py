from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from models import Product
from schemas import ProductCreate, ProductUpdate
from database import SessionLocal
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Drill 3: Idempotent Upserts

# SQLite implementation
def upsert_product_sqlite(db: Session, product_data: ProductCreate) -> Product:
    # Check if product exists
    product = db.query(Product).filter(
        Product.name == product_data.name,
        Product.deleted_at == None
    ).first()
    
    if product:
        # Update existing product
        product.description = product_data.description
        product.price = product_data.price
        logger.info(f"Updated product: {product.name}")
    else:
        # Insert new product
        product = Product(**product_data.dict())
        db.add(product)
        logger.info(f"Created new product: {product_data.name}")
    
    db.commit()
    db.refresh(product)
    return product

# PostgreSQL implementation (simulated)
def upsert_product_postgres(db: Session, product_data: ProductCreate) -> Product:
    # In a real PostgreSQL database, we would use something like:
    # INSERT INTO products (name, description, price) 
    # VALUES (:name, :description, :price)
    # ON CONFLICT (name) 
    # DO UPDATE SET description = :description, price = :price;
    
    # For our SQLite example, we'll use the SQLite approach
    return upsert_product_sqlite(db, product_data)

if __name__ == "__main__":
    db = SessionLocal()
    
    # Create initial product
    product_data = ProductCreate(
        name="Test Product",
        description="Initial description",
        price=10.99
    )
    
    product = upsert_product_sqlite(db, product_data)
    print(f"Initial product: {product.name}, Price: {product.price}")
    
    # Update the same product
    updated_data = ProductCreate(
        name="Test Product",
        description="Updated description",
        price=12.99
    )
    
    updated_product = upsert_product_sqlite(db, updated_data)
    print(f"Updated product: {updated_product.name}, Price: {updated_product.price}")
    
    db.close()
