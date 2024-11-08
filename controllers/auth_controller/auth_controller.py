from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.auth.auth import SignInPayload, SignUpPayload
from repositories.user_repository.user_repository import UserRepository
from utils.auth import Token
from database import get_db

router = APIRouter()

@router.post("/sign_in")
async def sign_in(data: SignInPayload, db: Session = Depends(get_db)):
    user = UserRepository.get_by_email(db, data.email)
    if user and user.check_password(data.password):
        token = Token.generate_and_sign(user.id)
        return {"message": "Login successful", "token": token}
    else:
        raise HTTPException(status_code=400, detail="Oops...wrong password or email")

@router.post("/sign_up")
async def sign_up(data: SignUpPayload, db: Session = Depends(get_db)):
    if data.password != data.password_confirm:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    if UserRepository.get_by_email(db, data.email):
        raise HTTPException(status_code=400, detail="User already registered")

    user = UserRepository.save(db, email=data.email, password=data.password)
    token = Token.generate_and_sign(user.id)
    return {"message": "Registration successful", "token": token}
