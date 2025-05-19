from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import logging
from datetime import datetime

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Drill 7: Schema-First vs Code-First Modeling

# In a Schema-First approach, we start with an existing schema

# This would typically be a schema definition from another team
EXISTING_SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    department_id INTEGER,
    hire_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    location TEXT
);
"""

def schema_first_approach():
    # Create an in-memory database with the existing schema
    engine = create_engine("sqlite:///:memory:")
    
    # Execute the schema creation SQL
    with engine.connect() as conn:
        conn.execute(EXISTING_SCHEMA_SQL)
        conn.commit()
    
    # Use reflection to create models from the existing schema
    metadata = MetaData()
    metadata.reflect(bind=engine)
    
    # Create SQLAlchemy models from reflected tables
    Base = declarative_base()
    
    class Employee(Base):
        __table__ = metadata.tables['employees']
        department = relationship("Department", back_populates="employees")
    
    class Department(Base):
        __table__ = metadata.tables['departments']
        employees = relationship("Employee", back_populates="department")
    
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Use the models
    # Insert a department
    eng_dept = Department(name="Engineering", location="Building A")
    session.add(eng_dept)
    session.commit()
    
    # Insert an employee
    employee = Employee(first_name="John", last_name="Doe", department_id=eng_dept.id)
    session.add(employee)
    session.commit()
    
    # Query
    employees = session.query(Employee).join(Department).all()
    for emp in employees:
        print(f"Employee: {emp.first_name} {emp.last_name}, Department: {emp.department.name}")
    
    print("\nSchema-First vs Code-First Approaches:\n")
    print("Schema-First Approach:")
    print("- Start with an existing database schema")
    print("- Use reflection or manual table definitions to match the schema")
    print("- Good for working with legacy databases")
    print("- Better when multiple applications share the same database")
    print("- Database schema is the source of truth")
    
    print("\nCode-First Approach:")
    print("- Define models in code first")
    print("- Generate database schema from models")
    print("- More flexible for evolving applications")
    print("- Better for new projects")
    print("- Code is the source of truth")
    
    print("\nWhen to use each approach:")
    print("Use Schema-First when:")
    print("- Working with existing databases")
    print("- In organizations with separate DBA teams")
    print("- When database schema changes are strictly controlled")
    
    print("\nUse Code-First when:")
    print("- Building new applications")
    print("- Rapid development is required")
    print("- Using modern development practices like TDD")
    print("- When the application owns the database")

if __name__ == "__main__":
    schema_first_approach()
