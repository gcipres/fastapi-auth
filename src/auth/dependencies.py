import time
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from src.auth import services as auth_services
from src.auth.schemas import UserSession
from src.users import services as users_services
from src.utils import constants

oauth2 = OAuth2PasswordBearer(tokenUrl="auth")

async def auth_user(token: str = Depends(oauth2)) -> UserSession:
    try:
        access_token = jwt.decode(token, constants.SECRET, algorithms=constants.ENCRYPT_ALGORITHM)
        username: str = access_token.get("sub")
        token_expiration: float = access_token.get("exp")

        if username is None:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=constants.JWT_INVALID)

        if token_expiration < time.time():
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=constants.JWT_EXPIRED)

        user = users_services.get_user(username)
        if not user:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=constants.JWT_INVALID)

        return auth_services.create_session_object(user)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=constants.JWT_EXPIRED)