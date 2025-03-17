from datetime import datetime, timezone
from sqlalchemy import Column, String, ForeignKey, Date, Boolean, TIMESTAMP, Float
from sqlalchemy.dialects.postgresql import ARRAY
from database import Base

class UserPublicInfo(Base):
    __tablename__ = "user_public_info"

    user_id = Column(String, ForeignKey('users.id', ondelete="CASCADE"), 
                     primary_key=True, nullable=False, unique=True, index=True)
    name = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String, nullable=False)  # Example values: "male", "female", "non-binary"
    looking_for = Column(ARRAY(String), nullable=False, default=[])  # Example: ["female", "non-binary"]
    description = Column(String, nullable=True)
    photos = Column(ARRAY(String), nullable=False, default=[])
    travel_list = Column(ARRAY(String), nullable=False, default=[])
    interests = Column(ARRAY(String), nullable=False, default=[])
    
    # Social Media Integration
    instagram = Column(String, nullable=True)  # Instagram username
    spotify = Column(String, nullable=True)  # Spotify username for music taste

    # Location for proximity-based matching
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    # Profile visibility settings
    profile_visibility = Column(Boolean, default=True)  # True = Visible, False = Hidden

    # Activity tracking
    last_active = Column(TIMESTAMP, default=lambda: datetime.now(timezone.utc))  # Last seen online

    # Timestamps for tracking
    created_at = Column(TIMESTAMP, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(TIMESTAMP, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))