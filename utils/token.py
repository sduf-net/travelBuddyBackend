import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "my_secret_key"
ALGORITHM = "HS256"

class Token:
    @staticmethod
    def generate_and_sign(user_id: str) -> str:
        expire = datetime.now(timezone.utc) + timedelta(days=1)
        payload = {"user_id": user_id, "exp": expire}
        
        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    def verify_token(token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None