# pylint: disable=C0114,C0116
import uuid
import datetime
from database import get_db
from utils.token import Token
from models.user.user import User
from sqlalchemy.orm import Session
from sduf.api_client import send_event
from sqlalchemy.exc import IntegrityError
from models.user_info.user_info import UserInfo
from fastapi import APIRouter, Depends, Response
from mailjet.mailjet_client import send_forgot_password_email
from schemas.sduf_request.sduf_request import SdufRequest, SdufEvent
from repositories.user_repository.user_repository import UserRepository
from repositories.user_info_repository.user_info_repository import UserInfoRepository
from models.user_forgot_password_code.user_forgot_password_code import UserForgotPasswordCode
from repositories.user_forgot_password_code_repository.user_forgot_password_code_repository import UserForgotPasswordCodeRepository

router = APIRouter()


@router.post("/sign_in")
async def sign_in(params: SdufRequest, db: Session = Depends(get_db)):
    try:
        if 'data' not in params.payload:
            raise ValueError("Missing required fields (email, password)")

        data = params.payload['data']
        # Validate that email and password are present
        if not data or 'email' not in data or 'password' not in data:
            raise ValueError("Missing required fields (email, password)")

        if '@' not in data['email'] or '.' not in data['email']:
            raise ValueError("Invalid email format")

        # Authenticate user
        user = UserInfoRepository.get_by_email(db, data['email'])
        user_forgot_password_code = None
        if user and user.check_password(data['password']):
            # Generate a token for the user if authentication is successful
            token = Token.generate_and_sign(user_id=str(user.id))

            event = SdufEvent(
                event_id=str(uuid.uuid4()),
                user_id=params.user_id,
                project_id=params.project_id,
                screen_id=params.screen_id,
                action="login",
                payload={"id": user.id, "token": token}
            )
            send_event(event)

            # Navigate to the index screen
            event = SdufEvent(
                event_id=str(uuid.uuid4()),
                user_id=params.user_id,
                project_id=params.project_id,
                screen_id=params.screen_id,
                action="navigate_to_screen",
                payload={
                    "screen_name": "index",
                    "params": {}
                }
            )
            send_event(event)
            return Response(status_code=204)
        else:
            raise ValueError("Incorrect email or password")
    except ValueError as e:
        error_message = str(e)
        # If authentication fails, send an error message
        event = SdufEvent(
            event_id=str(uuid.uuid4()),
            user_id=params.user_id,
            project_id=params.project_id,
            screen_id=params.screen_id,
            action="show_error_message",
            payload={"error_message": error_message}
        )
        send_event(event)
        return {"error_message": error_message}


@router.post("/sign_up")
async def sign_up(params: SdufRequest, db: Session = Depends(get_db)):
    try:
        if 'data' not in params.payload:
            raise ValueError("Missing required fields")

        data = params.payload['data']
        # Validate that email and password are present
        if not data or 'email' not in data or 'password' not in data:
            raise ValueError("Missing required fields")
        
        if 'full_name' not in data:
            raise ValueError("Missing Full Name")
        
        if 'phone_number' not in data:
            raise ValueError("Missing Phone Number")

        if '@' not in data['email'] or '.' not in data['email']:
            raise ValueError("Invalid email format")

        # Check if passwords match
        if data['password'] != data['password_confirm']:
            raise ValueError("Passwords do not match")

        # Check if the user already exists
        if UserInfoRepository.get_by_email(db, data['email']):
            raise ValueError("User already registered")

        user = User()
        user_info = UserInfo(user_id=str(user.id),
                             email=data['email'], 
                             password=data['password'])
        
        user_info = UserInfo.with_phone(user_info, data['phone_number'])
        user_info = UserInfo.with_full_name(user_info, data['full_name'])
        # Create the new user
        user = UserRepository.save(db, user)
        user_info = UserInfoRepository.save(db, user_info)

        token = Token.generate_and_sign(user_id=str(user.id))
        # Send login success event
        event = SdufEvent(
            event_id=str(uuid.uuid4()),
            user_id=params.user_id,
            project_id=params.project_id,
            screen_id=params.screen_id,
            action="login",
            payload={"id": user.id, "token": token}
        )
        send_event(event)

        # Navigate to the index screen
        event = SdufEvent(
            event_id=str(uuid.uuid4()),
            user_id=params.user_id,
            project_id=params.project_id,
            screen_id=params.screen_id,
            action="navigate_to_screen",
            payload={
                "screen_name": "index",
                "params": {
                    "current_date": int(datetime.datetime.now().timestamp())
                }
            }
        )
        send_event(event)

        return Response(status_code=204)
    except ValueError as e:
        error_message = str(e)
        # If authentication fails, send an error message
        event = SdufEvent(
            event_id=str(uuid.uuid4()),
            user_id=params.user_id,
            project_id=params.project_id,
            screen_id=params.screen_id,
            action="show_error_message",
            payload={"error_message": error_message}
        )
        send_event(event)
        return {"error_message": error_message}

@router.post("/forgot_password")
async def forgot_password(params: SdufRequest, db: Session = Depends(get_db)):
    try:
        if 'data' not in params.payload:
            raise ValueError("Missing required fields")

        data = params.payload['data']

        if 'email' not in data:
            raise ValueError("Missing email field")
        
        user = UserInfoRepository.get_by_email(db, data['email'])
        user_forgot_password_code = None
        if user:
            user_forgot_password_code = UserForgotPasswordCode(user_id=user.user_id)
            user_forgot_password_code = UserForgotPasswordCodeRepository.save(db, user_forgot_password_code)

        if user_forgot_password_code:
            send_forgot_password_email(full_name=user.full_name, code=user_forgot_password_code.code, send_to=data['email'], )

        event = SdufEvent(
            event_id=str(uuid.uuid4()),
            user_id=params.user_id,
            project_id=params.project_id,
            screen_id=params.screen_id,
            action="navigate_to_screen",
            payload={
                "screen_name": "forgot_password_code_validation",
                "params": {}
            }
        )
        send_event(event)
        return Response(status_code=204)
    except ValueError as e:
        error_message = str(e)

        event = SdufEvent(
            event_id=str(uuid.uuid4()),
            user_id=params.user_id,
            project_id=params.project_id,
            screen_id=params.screen_id,
            action="show_error_message",
            payload={"error_message": error_message}
        )
        send_event(event)
        return {"error_message": error_message}
    except IntegrityError as e:
        event = SdufEvent(
            event_id=str(uuid.uuid4()),
            user_id=params.user_id,
            project_id=params.project_id,
            screen_id=params.screen_id,
            action="show_error_message",
            payload={"error_message": f"Error: {str(e)}"}
        )

        if 'foreign key constraint' in str(e.orig):
            event = SdufEvent(
                event_id=str(uuid.uuid4()),
                user_id=params.user_id,
                project_id=params.project_id,
                screen_id=params.screen_id,
                action="show_error_message",
                payload={"error_message": "User with this email does not exisit"}
        )
        send_event(event)
        return {"error_message": {str(e)}}

@router.post("/forgot_password_verify_code")
async def forgot_password_verify_code(params: SdufRequest, db: Session = Depends(get_db)):
    print(params.payload)
    try:
        if 'data' not in params.payload:
            raise ValueError("Missing required fields")

        data = params.payload['data']

        if not data or 'code' not in data:
            raise ValueError("Missing code")

        user_code = UserForgotPasswordCodeRepository.get_valid_code(db, code=data['code'])
        if user_code:
            # Generate a token for the user if authentication is successful
            token = Token.generate_and_sign(user_id=str(user_code.user_id))

            event = SdufEvent(
                event_id=str(uuid.uuid4()),
                user_id=params.user_id,
                project_id=params.project_id,
                screen_id=params.screen_id,
                action="login",
                payload={"id": user_code.user_id, "token": token}
            )
            send_event(event)

            # Navigate to the index screen
            event = SdufEvent(
                event_id=str(uuid.uuid4()),
                user_id=params.user_id,
                project_id=params.project_id,
                screen_id=params.screen_id,
                action="navigate_to_screen",
                payload={
                    "screen_name": "index",
                    "params": {}
                }
            )
            send_event(event)
        return Response(status_code=204)
    except ValueError as e:
        error_message = str(e)
        event = SdufEvent(
            event_id=str(uuid.uuid4()),
            user_id=params.user_id,
            project_id=params.project_id,
            screen_id=params.screen_id,
            action="show_error_message",
            payload={"error_message": error_message}
        )
        send_event(event)
        return {"error_message": error_message}