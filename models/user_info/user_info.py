import uuid
from sqlalchemy import Column, String, ForeignKey, Text
from sqlalchemy.dialects.postgresql import ARRAY, JSON
from sqlalchemy.orm import relationship
from database import Base


class UserInfo(Base):
    __tablename__ = "user_info"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    bio = Column(Text, nullable=True)
    gender = Column(String, nullable=True)
    pictures = Column(ARRAY(String), nullable=True)
    geo = Column(JSON, nullable=True)

    def __init__(self, user_id: str, bio: str, gender: str, pictures: list | None = None, geo: dict | None = None):
        self.user_id = user_id
        self.bio = bio
        self.gender = gender
        self.pictures = pictures
        self.geo = geo

    def with_pictures(self, pictures: list | None = None):
        self.pictures = pictures
        return self

    def with_geo(self, geo: dict | None = None):
        self.geo = geo
        return self
