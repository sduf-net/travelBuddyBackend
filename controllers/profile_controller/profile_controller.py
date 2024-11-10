from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.sduf_request.sduf_request import SdufRequest
from repositories.user_repository.user_repository import UserRepository
from database import get_db
from sduf.api_client import send_event
import uuid

router = APIRouter()

@router.post("")
async def profile(params: SdufRequest, db: Session = Depends(get_db)):
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

    data = {
          "event_id": str(uuid.uuid4()),
          "user_id": params.user_id,
          "project_id": params.project_id,
          "screen_id": params.screen_id,
          "action": "replace",
          "payload": {"parent_id": params.payload["parent_id"], "widget": widget}
    }

    send_event(data)
    return {"message": "OK"}

@router.post("/edit")
async def profile_edit(params: SdufRequest, db: Session = Depends(get_db)):
     return {"message": "Implement me"}
