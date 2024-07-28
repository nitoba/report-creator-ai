from contextlib import _GeneratorContextManager
from http import HTTPStatus

from fastapi import Depends, HTTPException
from jwt import DecodeError, ExpiredSignatureError, decode
from sqlalchemy import select
from sqlalchemy.orm import Session
from typing_extensions import Annotated

from src.database.connection import get_db
from src.database.models import UserModel
from src.env import env
from src.http.common.dtos.user_public import UserPublic
from src.http.routes.auth.auth_bearer import JWTBearer

jwt_bearer = JWTBearer()


def get_current_user(
    session: _GeneratorContextManager[Session] = Depends(get_db),
    token: str = Depends(jwt_bearer),
):
    credentials_exception = HTTPException(
        status_code=HTTPStatus.UNAUTHORIZED,
        detail='Could not validate credentials',
    )

    try:
        payload = decode(token, env.JWT_SECRET, algorithms=['HS256'])
        sub: str = payload.get('sub')
        if not sub:
            raise credentials_exception
    except DecodeError:
        raise credentials_exception
    except ExpiredSignatureError:
        raise credentials_exception

    with session as db:
        user = db.execute(select(UserModel).filter_by(id=sub)).scalar_one_or_none()

    if not user:
        raise credentials_exception

    return user


CurrentUser = Annotated[UserPublic, Depends(get_current_user)]
