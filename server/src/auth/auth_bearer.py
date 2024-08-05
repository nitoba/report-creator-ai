from http import HTTPStatus

from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt import decode

from src.env import env


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(
            request
        )
        if credentials:
            if not credentials.scheme == 'Bearer':
                raise HTTPException(
                    status_code=HTTPStatus.FORBIDDEN,
                    detail='Invalid authentication scheme.',
                )
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(
                    status_code=HTTPStatus.FORBIDDEN,
                    detail='Invalid token or expired token.',
                )
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail='Invalid authorization code.')

    def verify_jwt(self, token: str) -> bool:
        isTokenValid: bool = False

        try:
            payload = decode(token, env.JWT_SECRET, algorithms=['HS256'])
            sub: str = payload.get('sub')
            if not sub:
                raise HTTPException(
                    status_code=HTTPStatus.UNAUTHORIZED,
                    detail='Could not validate credentials',
                )
        except Exception as e:
            print(f'Error verifying token: {e}')
            payload = None
        if payload:
            isTokenValid = True

        return isTokenValid
