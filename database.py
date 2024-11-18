from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import get_settings

engine = create_engine(get_settings().DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """Get a session for interacting with the database"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()