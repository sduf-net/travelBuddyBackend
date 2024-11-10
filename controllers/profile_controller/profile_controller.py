from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.sduf_request.sduf_request import SdufRequest
from repositories.user_repository.user_repository import UserRepository
from database import get_db

router = APIRouter()

@router.post("")
async def profile(params: SdufRequest, db: Session = Depends(get_db)):
    return {"message": "Implement me"}

@router.post("/edit")
async def profile_edit(params: SdufRequest, db: Session = Depends(get_db)):
     return {"message": "Implement me"}
