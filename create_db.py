import os
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings
from database import Base
from models import user

# Define the database URL for PostgreSQL (without the database name, just the connection)
DATABASE_URL = os.getenv("DATABASE_URL_CREATE", "postgresql://postgres:postgres@db/")
DATABASE_NAME = "travel_buddy_db"  # Database name to be created
TEST_DATABASE_NAME = "test_travel_buddy_db"  # Database name to be created

# Create the engine to connect to PostgreSQL (without specifying the database)
engine = create_engine(DATABASE_URL, isolation_level="AUTOCOMMIT", pool_pre_ping=True)

# Create a session maker for database interaction
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to create the database if it does not exist
def create_database():
    try:
        # Connect to PostgreSQL server and create the database
        with engine.connect() as connection:
            connection.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}")
            connection.execute(f"CREATE DATABASE IF NOT EXISTS {TEST_DATABASE_NAME}")
            print(f"Database '{DATABASE_NAME}' created successfully.")
            print(f"Database '{TEST_DATABASE_NAME}' created successfully.")
    except OperationalError as e:
        print(f"Error: {e}")
        # If the database already exists, this exception will be triggered.

# Function to create the tables in the newly created database
def create_tables():
    # Update the database URL to include the database name
    db_url_with_db = f"{DATABASE_URL}"
    engine_with_db = create_engine(db_url_with_db)

    # Create tables based on the models defined
    try:
        Base.metadata.create_all(bind=engine_with_db)  # This will create all the tables in the database
        print(f"Tables created successfully in the database '{DATABASE_NAME}'.")
    except Exception as e:
        print(f"Error while creating tables: {e}")

# Main execution to create the database and tables
if __name__ == "__main__":
    # Create the database if it does not exist
    create_database()

    # After database creation, connect to it and create tables
    create_tables()
