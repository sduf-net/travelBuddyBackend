import uuid
import os
import json
from fastapi import FastAPI, Response
from fastapi.exceptions import RequestValidationError
from database import Base, engine
from controllers.auth_controller import auth_controller
from controllers.profile_controller import profile_controller
from controllers.explore_controller import explore_controller
from controllers.chat_controller import chat_controller
from schemas.sduf_request.sduf_request import SdufEvent
from sduf.api_client import send_event
from create_db import create_database

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    error_messages = []

    for error in exc.errors():
        ctx = error.get("ctx")
        if isinstance(ctx, dict) and 'reason' in ctx:
            error_message = ctx['reason']
            error_messages.append(error_message)

    all_errors = "\n".join(error_messages)

    body = await request.body()
    body_str = body.decode()
    params = json.loads(body_str)

    event = SdufEvent(
        event_id=str(uuid.uuid4()),
        user_id=params['user_id'],
        project_id=params['project_id'],
        screen_id=params['screen_id'],
        action="show_error_message",
        payload={"error_message": all_errors}
    )
    send_event(event)
    
    return Response(status_code=204)


if not os.getenv("ENV"):
    os.environ["ENV"] = "dev"

create_database()
# Initialize the database
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth_controller.router, prefix="/auth", tags=["auth"])
app.include_router(profile_controller.router, prefix="/profile", tags=["profile"])
app.include_router(chat_controller.router, prefix="/chat", tags=["chat"])
app.include_router(explore_controller.router, prefix="/explore", tags=["explore"])