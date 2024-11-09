from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """Get a session for interacting with the database"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to create the test database schema
def create_test_db():
    """Create the test database schema."""
    test_engine = create_engine(settings.TEST_DATABASE_URL)  # Use the test database URL
    Base.metadata.create_all(bind=test_engine)  # Create all tables for the test database

# Function to drop the test database schema
def drop_test_db():
    """Drop the test database schema."""
    test_engine = create_engine(settings.TEST_DATABASE_URL)  # Use the test database URL
    Base.metadata.drop_all(bind=test_engine)  # Drop all tables for the test database
