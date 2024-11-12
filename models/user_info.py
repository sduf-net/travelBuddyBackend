from sqlalchemy import Column, String, ForeignKey, Text
from sqlalchemy.dialects.postgresql import ARRAY, JSON
from sqlalchemy.orm import relationship
from database import Base
import uuid

class UserInfo(Base):
    __tablename__ = "user_info"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    bio = Column(Text, nullable=True)
    pictures = Column(ARRAY(String), nullable=True)
    geo = Column(JSON, nullable=True)

    user = relationship("User", back_populates="user_info")
