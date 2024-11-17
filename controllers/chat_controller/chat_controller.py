from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.sduf_request.sduf_request import SdufRequest
from repositories.user_repository.user_repository import UserRepository
from database import get_db
from utils.randomizer import get_random_image, get_random_woman_name
import uuid

router = APIRouter()

@router.post("/list")
async def profile(params: SdufRequest, db: Session = Depends(get_db)):
    chat_preview = {
        "data": {
            "actions": {
                "click": {
                    "screen_name": "index",
                    "type": "route_to_local"
                },
                "long_press": {
                    "params": {
                        "parameter": "parameter"
                    },
                    "type": "async_post",
                    "url": "url"
                }
            },
            "date": "2021.01.01",
            "src": get_random_image(),
            "text": "Lorem ipsum dolor sit amet, consectetur",
            "title": get_random_woman_name()
        },
        "id": str(uuid.uuid4()),
        "memo": "",
        "name": "ChatPreviewWidget"
    }
    api_widget = {
        "id": str(uuid.uuid4()),
        "name": "ApiWidget",
        "data": {
            "callbackUrl": "{{HOST}}/chat/list"
        }
    }
    return [chat_preview, api_widget]

@router.post("/{chat_id}}")
async def profile_edit(params: SdufRequest, db: Session = Depends(get_db)):
     return {"message": "Implement me"}
