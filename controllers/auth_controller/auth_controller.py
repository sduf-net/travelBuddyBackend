from fastapi import APIRouter, HTTPException, Depends, Response
from sqlalchemy.orm import Session
from schemas.auth.auth import SignInPayload, SignUpPayload
from repositories.user_repository.user_repository import UserRepository
from utils.token import Token
from database import get_db
from schemas.sduf_request.sduf_request import SdufEvent
import uuid
from sduf.api_client import send_event

router = APIRouter()

@router.post("/sign_in")
async def sign_in(params: SignInPayload, db: Session = Depends(get_db)):
    data = params.payload.data

    user = UserRepository.get_by_email(db, data.email)
    if user and user.check_password(data.password):
        token = Token.generate_and_sign(user.id)

        event = SdufEvent(
            event_id=str(uuid.uuid4()),
            user_id=params.user_id,
            project_id=params.project_id,
            screen_id=params.screen_id,
            action="login",
            payload={"id": user.id, "token": token}
        )
        send_event(event.model_dump())
        return Response(status_code=204)
    else:
        event = SdufEvent(
            event_id=str(uuid.uuid4()),
            user_id=params.user_id,
            project_id=params.project_id,
            screen_id=params.screen_id,
            action="show_error_message",
            payload={"error_message": "Oops...wrong password or email"}
        )
        send_event(event.model_dump())
        return Response(status_code=204)

@router.post("/sign_up")
async def sign_up(params: SignUpPayload, db: Session = Depends(get_db)):
    data = params.payload.data
    action = None

    if data.password != data.password_confirm:
        action="show_error_message"
        payload={"error_message": "Passwords do not match"}

    if UserRepository.get_by_email(db, data.email):
        action="show_error_message"
        payload={"error_message": "User already registered"}

    if action == "show_error_message":
        event = SdufEvent(
            event_id=str(uuid.uuid4()),
            user_id=params.user_id,
            project_id=params.project_id,
            screen_id=params.screen_id,
            action=action,
            payload=payload
        )
        send_event(event.model_dump())
        return Response(status_code=204)

    user = UserRepository.save(db, email=data.email, password=data.password)
    token = Token.generate_and_sign(user.id)

    event = SdufEvent(
        event_id=str(uuid.uuid4()),
        user_id=params.user_id,
        project_id=params.project_id,
        screen_id=params.screen_id,
        action="login",
        payload={"id": user.id, "token": token}
    )
    send_event(event.model_dump())

    event = SdufEvent(
        event_id=str(uuid.uuid4()),
        user_id=params.user_id,
        project_id=params.project_id,
        screen_id=params.screen_id,
        action="close_popup",
        payload={}
    )
    send_event(event.model_dump())

    return Response(status_code=204)
