from fastapi import HTTPException, status, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from models.user.user import User
from database import get_db
from typing import Annotated
from utils.token import Token

class TokenRequest(BaseModel):
    user_token: str

def get_current_user(params: TokenRequest, db: Annotated[Session, Depends(get_db)]) -> User:
    """ Dependency to get the current user from the token """
    payload = Token.verify_token(params.user_token)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")

    user_id = payload.get("user_id")
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload")

    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    if user.is_deleted is True:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User is deleted")

    if user.is_archived is True:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User is archived")

    return user
