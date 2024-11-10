import os

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db/travel_buddy_db")
    TEST_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db/test_travel_buddy_db")
    SDUF_BASE_URL = os.getenv("SDUF_BASE_URL", "https://sduf.net")
    SDUF_PROJECT_TOKEN = os.getenv("SDUF_PROJECT_TOKEN", "N4DBMiKlJXbpStsZrHwHyX1nkxw9RAvurP3GgwnHuOc=")
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")

settings = Settings()
