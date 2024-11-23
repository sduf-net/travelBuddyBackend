import uuid
from sqlalchemy import Column, String, ForeignKey, DateTime, Text, func
from sqlalchemy.orm import relationship
from database import Base


class Message(Base):
    __tablename__ = 'messages'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    conversation_id = Column(String, ForeignKey(
        'conversations.id', ondelete='CASCADE'), nullable=False)
    sender_id = Column(String, ForeignKey(
        'users.id', ondelete='CASCADE'), nullable=False)
    content = Column(Text, nullable=False)
    reply_to_id = Column(String, ForeignKey(
        'messages.id', ondelete='SET NULL'))
    message_type = Column(String(20), default='text')
    created_at = Column(DateTime, server_default=func.now())

    # conversation = relationship('Conversation', back_populates='messages')
    # sender = relationship('User', foreign_keys=[sender_id])
    # reply_to = relationship('Message', remote_side=[id])

    def __init__(self, conversation_id: str, sender_id: str, content: str, reply_to_id: str | None = None, message_type: str = "text"):
        self.conversation_id = conversation_id
        self.sender_id = sender_id
        self.content = content
        self.reply_to_id = reply_to_id
        self.message_type = message_type
