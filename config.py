import os
from functools import lru_cache

class Settings:
    """Production settings class"""
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db/")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "travel_buddy_prod")
    SDUF_BASE_URL = os.getenv("SDUF_BASE_URL", "https://sduf.net")
    SDUF_PROJECT_TOKEN = os.getenv("SDUF_PROJECT_TOKEN", "XRHO7CqVHALu/zpp9j5NhJLdZQkqs/MMVKE0AdAy+j8=")
    SECRET_KEY = os.getenv("SECRET_KEY", "prod-secret-key")

    MJ_APIKEY_PUBLIC = os.getenv("MJ_APIKEY_PUBLIC")
    MJ_APIKEY_PRIVATE = os.getenv("MJ_APIKEY_PRIVATE")

class DevSettings(Settings):
    """Development settings class"""
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db/")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "travel_buddy_dev")

class TestSettings(Settings):
    """Test settings class"""
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db/")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "travel_buddy_test")
    MJ_APIKEY_PUBLIC = os.getenv("MJ_APIKEY_PUBLIC", "")
    MJ_APIKEY_PRIVATE = os.getenv("MJ_APIKEY_PRIVATE", "")

@lru_cache
def get_settings():
    """Return settings based on ENV variable"""
    env = os.getenv("ENV", "dev")
    if env == "test":
        return TestSettings()
    elif env == "dev":
        return DevSettings()
    return Settings()  # Default to production settings
