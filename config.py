import os

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db/travel_buddy_db")
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")

settings = Settings()
