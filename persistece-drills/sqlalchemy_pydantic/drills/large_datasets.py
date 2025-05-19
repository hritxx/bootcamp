from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
import time
import psutil
import os
from models import Product, Base
from database import engine, SessionLocal
import logging
import random

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Drill 9: Boundary Testing with Large Datasets

def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024  # in MB

def generate_product_data(count: int = 10000):
    products = []
    for i in range(count):
        products.append({
            "name": f"Product {i}",
            "description": f"This is product {i}",
            "price": round(random.uniform(1.0, 1000.0), 2)
        })
    return products

# Naive approach - single inserts
def insert_products_naive(db: Session, products: list[dict]):
    start_time = time.time()
    start_memory = get_memory_usage()
    
    for product_data in products:
        product = Product(**product_data)
        db.add(product)
        db.commit()
    
    end_time = time.time()
    end_memory = get_memory_usage()
    
    logger.info(f"Naive insertion of {len(products)} products:")
    logger.info(f"- Time taken: {end_time - start_time:.2f} seconds")
    logger.info(f"- Memory used: {end_memory - start_memory:.2f} MB")
    
    return end_time - start_time, end_memory - start_memory

# Batch approach - using transactions
def insert_products_batch(db: Session, products: list[dict], batch_size: int = 1000):
    start_time = time.time()
    start_memory = get_memory_usage()
    
    total = len(products)
    for i in range(0, total, batch_size):
        batch = products[i:min(i + batch_size, total)]
        db.bulk_insert_mappings(Product, batch)
        db.commit()
    
    end_time = time.time()
    end_memory = get_memory_usage()
    
    logger.info(f"Batch insertion of {len(products)} products (batch size: {batch_size}):")
    logger.info(f"- Time taken: {end_time - start_time:.2f} seconds")
    logger.info(f"- Memory used: {end_memory - start_memory:.2f} MB")
    
    return end_time - start_time, end_memory - start_memory

# Raw SQL approach
def insert_products_raw_sql(products: list[dict], batch_size: int = 1000):
    start_time = time.time()
    start_memory = get_memory_usage()
    
    conn = engine.connect()
    
    total = len(products)
    for i in range(0, total, batch_size):
        batch = products[i:min(i + batch_size, total)]
        
        # Prepare values string for the INSERT statement
        values = []
        for p in batch:
            values.append(f"('{p['name']}', '{p['description']}', {p['price']})")
        
        values_str = ", ".join(values)
        
        sql = f"""
        INSERT INTO products (name, description, price)
        VALUES {values_str}
        """
        
        conn.execute(text(sql))
    
    conn.close()
    
    end_time = time.time()
    end_memory = get_memory_usage()
    
    logger.info(f"Raw SQL insertion of {len(products)} products (batch size: {batch_size}):")
    logger.info(f"- Time taken: {end_time - start_time:.2f} seconds")
    logger.info(f"- Memory used: {end_memory - start_memory:.2f} MB")
    
    return end_time - start_time, end_memory - start_memory

def stress_test():
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)
    
    # Clear products table
    db = SessionLocal()
    db.query(Product).delete()
    db.commit()
    db.close()
    
    # Generate product data - using a smaller number for demonstration
    # In a real test, we would use 1,000,000 records
    products = generate_product_data(1000)
    
    # Test naive approach with a small subset
    db = SessionLocal()
    naive_time, naive_memory = insert_products_naive(db, products[:10])
    db.close()
    
    # Clear products table
    db = SessionLocal()
    db.query(Product).delete()
    db.commit()
    db.close()
    
    # Test batch approach
    db = SessionLocal()
    batch_time, batch_memory = insert_products_batch(db, products)
    db.close()
    
    # Clear products table
    db = SessionLocal()
    db.query(Product).delete()
    db.commit()
    db.close()
    
    # Test raw SQL approach
    raw_time, raw_memory = insert_products_raw_sql(products)
    
    # Compare results
    print("\nPerformance Comparison (extrapolated for 1 million records):")
    print(f"Naive approach: {naive_time * 100000:.2f} seconds, {naive_memory * 100:.2f} MB")
    print(f"Batch approach: {batch_time * 1000:.2f} seconds, {batch_memory * 1000:.2f} MB")
    print(f"Raw SQL approach: {raw_time * 1000:.2f} seconds, {raw_memory * 1000:.2f} MB")
    
    print("\nWhy ORM patterns can fail at scale:")
    print("1. Individual transactions have high overhead")
    print("2. Session state grows with each tracked object")
    print("3. Memory usage increases with large result sets")
    print("4. ORM object creation has CPU cost")
    print("\nHow to monitor and profile performance:")
    print("1. Use database query execution plans/EXPLAIN")
    print("2. Monitor database connection pools")
    print("3. Use APM tools like New Relic or Datadog")
    print("4. Profile Python code with tools like cProfile")
    print("5. Monitor query times and implement query timeouts")

if __name__ == "__main__":
    stress_test()
