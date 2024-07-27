from server.src.database.models import UserModel

from src.database.connection import get_db


class UserRepository:
    def save(self, user: UserModel) -> None:
        with get_db() as db:
            db.add(user)
            db.commit()
            db.refresh(user)

    def find_by_email(self, email: str) -> UserModel | None:
        with get_db() as db:
            return db.query(UserModel).filter_by(email=email).first()

    def find_by_username(self, username: str) -> UserModel | None:
        with get_db() as db:
            return db.query(UserModel).filter_by(username=username).first()

    def find_by_id(self, user_id: str) -> UserModel | None:
        with get_db() as db:
            return db.query(UserModel).filter_by(id=user_id).first()
