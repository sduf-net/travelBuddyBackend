from sqlalchemy.orm import Session
from models.user_info.user_info import UserInfo


class UserInfoRepository:
    @staticmethod
    def save(session: Session, user_info: UserInfo):
        session.add(user_info)
        session.commit()
        return user_info

    @staticmethod
    def get_by_email(session: Session, email: str):
        return session.query(UserInfo).filter(UserInfo.email == email).first()

    @staticmethod
    def get_by_user_id(session: Session, user_id: str):
        return session.query(UserInfo).filter(UserInfo.user_id == user_id).first()
