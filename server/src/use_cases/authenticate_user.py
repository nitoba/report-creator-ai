from pydantic import BaseModel

from src.cryptography.argon2_hasher import Argon2Hasher
from src.cryptography.jwt_encrypter import JwtEncrypter
from src.database.repositories.user_repository import UserRepository
from src.http.common.dtos.user_public import UserPublic


class AuthenticateUserUseCaseRequest(BaseModel):
    email: str
    password: str


class AuthenticateUserUseCaseResponse(BaseModel):
    access_token: str
    user: UserPublic


class AuthenticateUserUseCase:
    def __init__(
        self,
        user_repository: UserRepository,
        hasher: Argon2Hasher,
        encrypter: JwtEncrypter,
    ):
        self.user_repository = user_repository
        self.hasher = hasher
        self.encrypter = encrypter

    def execute(
        self, request: AuthenticateUserUseCaseRequest
    ) -> AuthenticateUserUseCaseResponse:
        user_exists = self.user_repository.find_by_email(request.email)

        if not user_exists:
            raise Exception('Invalid credentials')

        passwords_match = self.hasher.compare(request.password, user_exists.password)

        if not passwords_match:
            raise Exception('Invalid credentials')
        token_payload = {
            'sub': user_exists.id,
            'username': user_exists.username,
            'email': user_exists.email,
        }
        access_token = self.encrypter.encrypt(token_payload)

        return AuthenticateUserUseCaseResponse(
            access_token=access_token, user=user_exists.to_public()
        )
