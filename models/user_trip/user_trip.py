from sqlalchemy import Column, String, ForeignKey, Date, Text, DateTime, func
from datetime import date
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
    updated_at = Column(DateTime, default=func.now(),
                        onupdate=func.now(), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)

    def __init__(
        self,
        user_id: str,
        start_date: date,
        end_date: date,
        country: str,
        province: str | None = None,
        city: str | None = None
    ):
        self.user_id = user_id
        self.start_date = start_date
        self.end_date = end_date
        self.country = country
        self.province = province
        self.city = city
