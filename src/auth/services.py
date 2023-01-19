from fastapi import HTTPException, status
from jose import jwt
from datetime import datetime, timedelta
from uuid import UUID
from src.auth.schemas import UserSession
from src.users.schemas import User
from src.utils import constants

def create_session_object(user: User) -> UserSession:
	access_token = {
        "sub": user.email,
        "exp": datetime.utcnow() + timedelta(minutes=constants.ACCESS_TOKEN_DURATION)
    }
	
	return UserSession(
        jwt=jwt.encode(access_token, constants.SECRET, algorithm=constants.ENCRYPT_ALGORITHM),
		id=user.id,
		name=user.name,
		email=user.email
    )