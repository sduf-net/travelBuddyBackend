import uuid
from sqlalchemy import Column, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from database import Base


class MessageReaction(Base):
    __tablename__ = 'message_reactions'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    message_id = Column(String, ForeignKey(
        'messages.id', ondelete='CASCADE'), nullable=False)
    user_id = Column(String, ForeignKey(
        'users.id', ondelete='CASCADE'), nullable=False)
    emoji = Column(String(10), nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    def __init__(self, user_id: str, message_id: str, emoji: str):
        self.user_id = user_id
        self.message_id = message_id
        self.emoji = emoji
