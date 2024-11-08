from pydantic import BaseModel, EmailStr

class SignUpPayload(BaseModel):
    class Payload(BaseModel):
        class Data(BaseModel):
            hashed_password: str
            password: str
            email: EmailStr
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
