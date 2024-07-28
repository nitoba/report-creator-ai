from datetime import datetime, timedelta

from jwt import DecodeError, decode, encode
from pydantic import BaseModel
from zoneinfo import ZoneInfo

from src.env import env

ACCESS_TOKEN_EXPIRE_MINUTES = 30
ALGORITHM = 'HS256'


class TokenPayload(BaseModel):
    sub: str
    username: str
    email: str
    exp: datetime


class JwtEncrypter:
    def encrypt(self, payload: dict) -> str:
        expire = datetime.now(tz=ZoneInfo('UTC')) + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
        to_encode = TokenPayload(**payload, exp=expire).model_dump()
        encoded_jwt = encode(to_encode, env.JWT_SECRET, algorithm=ALGORITHM)
        return encoded_jwt

    def decrypt(self, token: str) -> TokenPayload:
        try:
            payload = decode(token, env.JWT_SECRET, algorithms=[ALGORITHM])
            return TokenPayload(**payload)
        except DecodeError:
            raise Exception('Invalid token')
