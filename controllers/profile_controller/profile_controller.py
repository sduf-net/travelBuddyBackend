from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.sduf_request.sduf_request import SdufRequest
from database import get_db
from utils.current_user import get_current_user
from models.user import User

router = APIRouter()


@router.post("")
async def profile(
    params: SdufRequest,
    db: Session = Depends(get_db),
    current_user: Annotated[User | None, Depends(get_current_user)] = None
):
    widget = {
        "data": {
            "props": {
                "alignItems": "center",
                "justifyContent": "center",
                "mt": 40
            }
        },
        "id": "1845cb9e-4ad6-4ba3-b3f1-67b2ee7b4181",
        "memo": "",
        "name": "MangusDivWidget",
        "nestedComponents": [
            {
                "data": {
                    "props": {
                        "h": 100,
                        "m": 10,
                        "rounded": "circle",
                        "source": {
                            "uri": "https://images.unsplash.com/photo-1593642532400-2682810df593?ixid=MXwxMjA3fDF8MHxlZGl0b3JpYWwtZmVlZHwxfHx8ZW58MHx8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
                        },
                        "w": 100
                    }
                },
                "id": "880d86bb-2060-47f3-9391-60b9c606e958",
                "memo": "",
                "name": "MangusImageWidget"
            }
        ]
    }

    return [widget]


@router.post("/edit")
async def profile_edit(
    params: SdufRequest,
    db: Session = Depends(get_db),
    current_user: Annotated[User | None, Depends(get_current_user)] = None
):
    return {"message": "Implement me"}


@router.post("/me")
async def profile_me(
    params: SdufRequest,
    db: Session = Depends(get_db),
    current_user: Annotated[User | None, Depends(get_current_user)] = None
):
    return {"message": "Implement me"}


@router.post("/details")
async def profile_details(
    params: SdufRequest,
    db: Session = Depends(get_db),
    current_user: Annotated[User | None, Depends(get_current_user)] = None
):
    return {"message": "Implement me"}
