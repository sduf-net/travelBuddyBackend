from pydantic import BaseModel, EmailStr, field_validator
import re

class SignUpPayload(BaseModel):
    class Payload(BaseModel):
        class Data(BaseModel):
            password_confirm: str
            password: str
            email: EmailStr

            @field_validator("password")
            def validate_password(cls, password):
                # Check password length
                if len(password) < 8:
                    raise ValueError("Password must be at least 8 characters long")

                # Check for at least one digit
                if not any(char.isdigit() for char in password):
                    raise ValueError("Password must contain at least one digit")

                # Check for at least one uppercase letter
                if not any(char.isupper() for char in password):
                    raise ValueError("Password must contain at least one uppercase letter")

                # Check for at least one lowercase letter
                if not any(char.islower() for char in password):
                    raise ValueError("Password must contain at least one lowercase letter")

                # Check for at least one special character
                if not re.search(r"[#?!@$%^&*()]", password):
                    raise ValueError("Password must contain at least one special character")

                return password
        data: Data

    payload: Payload
    user_id: str
    screen_id: str
    project_id: str

class SignInPayload(BaseModel):
    class Payload(BaseModel):
        class Data(BaseModel):
            password: str
            email: EmailStr
        data: Data

    payload: Payload
    user_id: str
    screen_id: str
    project_id: str
