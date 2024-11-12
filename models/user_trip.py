from sqlalchemy import Column, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from database import Base
import uuid

class UserTrip(Base):
    __tablename__ = "user_trips"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    country = Column(String, nullable=False)
    province = Column(String, nullable=True)
    city = Column(String, nullable=True)
    private_note = Column(Text, nullable=True)
    public_note = Column(Text, nullable=True)

    # Relationship with User
    user = relationship("User", back_populates="user_trips")
