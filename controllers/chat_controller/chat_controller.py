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
async def chat_list(params: SdufRequest, db: Session = Depends(get_db)):
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
async def chat(params: SdufRequest, db: Session = Depends(get_db)):
    messages = []
    for _ in range(random.randint(10, 25)):
        message = ChatMessage(
            name=get_random_woman_name(),
            text="Lorem ipsum dolor sit amet, consectetur",
            date="2021.01.01",
            is_owner=get_random_boolean(),
            actions={}
        )
        messages.append(message)
    return messages


@router.post("/new")
async def new_message(params: SdufRequest, db: Session = Depends(get_db)):
    value = params.payload['params']['value']
    message = ChatMessage(
        name=get_random_woman_name(),
        text=value,
        date="2021.01.01",
        is_owner=True,
        actions={}
    )
    event = SdufEvent(
        event_id=str(uuid.uuid4()),
        user_id=params.user_id,
        project_id=params.project_id,
        screen_id=params.screen_id,
        action="append",
        payload={"widget": message.to_dict()}
    )
    send_event(event.model_dump())
    return Response(status_code=204)