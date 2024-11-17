from fastapi import APIRouter, Depends, Response
import random
from sqlalchemy.orm import Session
from schemas.sduf_request.sduf_request import SdufEvent, SdufRequest
from repositories.user_repository.user_repository import UserRepository
from database import get_db
from utils.randomizer import get_random_boolean, get_random_image, get_random_woman_name
import uuid
from components.chat_message import ChatMessage
from sduf.api_client import send_event

router = APIRouter()

@router.post("/list")
async def profile(params: SdufRequest, db: Session = Depends(get_db)):
    chat_preview = {
        "data": {
            "actions": {
                "click": {
                    "type": "navigate_to",
                    "screen_name": "chat",
                    "params": {
                        "chat_id": "this_is_chat_id"
                    }
                },
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

@router.post("/id")
async def profile_edit(params: SdufRequest, db: Session = Depends(get_db)):
    messages = []
    for _ in range(random.randint(10, 25)):
        data = {
            "name": get_random_woman_name(),
            "text": "Lorem ipsum dolor sit amet, consectetur",
            "date": "2021.01.01",
            "is_owner": get_random_boolean(),
            "actions": {}
        }
        message = ChatMessage(data=data)
        messages.append(message)
    return messages
