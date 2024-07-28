from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.cryptography.argon2_hasher import Argon2Hasher
from src.cryptography.jwt_encrypter import JwtEncrypter
from src.database.repositories.user_repository import UserRepository
from src.use_cases.authenticate_user import (
    AuthenticateUserUseCase,
    AuthenticateUserUseCaseRequest,
    AuthenticateUserUseCaseResponse,
)
from src.use_cases.register_user import (
    RegisterUserUseCase,
    RegisterUserUseCaseRequest,
    RegisterUserUseCaseResponse,
)

router = APIRouter(prefix='/auth', tags=['auth'])
hasher = Argon2Hasher()
jwt_encypter = JwtEncrypter()
user_repository = UserRepository()
authenticate_user_use_case = AuthenticateUserUseCase(
    user_repository, hasher, jwt_encypter
)
register_user_use_case = RegisterUserUseCase(user_repository, hasher)


@router.post('/authenticate', response_model=AuthenticateUserUseCaseResponse)
def authenticate(authenticate_body: AuthenticateUserUseCaseRequest):
    try:
        return authenticate_user_use_case.execute(authenticate_body)
    except Exception as error:
        return JSONResponse(status_code=400, content={'message': str(error)})


@router.post('/register', response_model=RegisterUserUseCaseResponse)
def register(create_user_body: RegisterUserUseCaseRequest):
    try:
        return register_user_use_case.execute(create_user_body)
    except Exception as error:
        return JSONResponse(status_code=400, content={'message': str(error)})
