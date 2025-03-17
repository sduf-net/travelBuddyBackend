from datetime import datetime
from sqlalchemy.orm import Session
from models.user_forgot_password_code.user_forgot_password_code import UserForgotPasswordCode


class UserForgotPasswordCodeRepository:
    @staticmethod
    def save(session: Session, user_forgot_password_code: UserForgotPasswordCode):
        session.add(user_forgot_password_code)
        session.commit()
        return user_forgot_password_code

    @staticmethod
    def validate_code(session: Session, user_id: str, code: str):
        row = session.query(UserForgotPasswordCode).filter(
            UserForgotPasswordCode.user_id == user_id, 
            UserForgotPasswordCode.code == code, 
            UserForgotPasswordCode.expired_at > datetime.now()
        ).first()

        if row:
            return True

        return False

    @staticmethod
    def get_valid_code(session: Session, code: str):
        return session.query(UserForgotPasswordCode).filter(
            UserForgotPasswordCode.code == code, 
            UserForgotPasswordCode.expired_at > datetime.now()
        ).first()