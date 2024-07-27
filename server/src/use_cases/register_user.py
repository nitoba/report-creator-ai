from datetime import datetime

from pydantic import BaseModel

from src.cryptography.argon2_hasher import Argon2Hasher
from src.database.models import UserModel
from src.database.repositories.user_repository import UserRepository


class RegisterUserUseCaseRequest(BaseModel):
    username: str
    email: str
    password: str


class RegisterUserUseCaseResponse(BaseModel):
    id: str
    username: str
    email: str
    created_at: datetime
    updated_at: datetime


class RegisterUserUseCase:
    def __init__(self, user_repository: UserRepository, hasher: Argon2Hasher):
        self.user_repository = user_repository
        self.hasher = hasher

    def execute(self, request: RegisterUserUseCaseRequest) -> RegisterUserUseCaseResponse:
        user_already_exists = self.user_repository.find_by_username(
            request.username
        ) or self.user_repository.find_by_email(request.email)

        if user_already_exists:
            raise Exception('User already exists')

        hashed_password = self.hasher.hash(request.password)

        user = UserModel(
            username=request.username,
            email=request.email,
            password=hashed_password,
        )

        print(user)

        self.user_repository.save(user)

        return RegisterUserUseCaseResponse(
            id=user.id,
            username=user.username,
            email=user.email,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )
