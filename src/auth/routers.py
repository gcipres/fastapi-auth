import logging
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from src.auth.schemas import UserSession
from src.auth import services as auth_services, dependencies as auth_dependencies
from src.users.schemas import User
from src.users import services as users_services
from src.utils import encrypt, constants

router = APIRouter()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s -%(name)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

@router.post("/auth/signup", status_code=status.HTTP_201_CREATED)
async def signup(access_data: User) -> User:
    logger.info(f"[signup] -> user: {access_data.email}")
    exist_email = users_services.check_email(access_data.email)
    if exist_email:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=constants.USER_ALREADY_EXIST)

    return users_services.create_user(access_data)

@router.post("/auth/signin", status_code=status.HTTP_201_CREATED)
async def signin(form: OAuth2PasswordRequestForm = Depends()) -> UserSession:
    logger.info(f"[signin with credentials] -> user: {form.username}")
    user = users_services.get_user(form.username)
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=constants.USER_DOES_NOT_EXIST)
    
    if not form.client_id and not encrypt.crypt.verify(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=constants.PASSWORD_INCORRECT)

    return auth_services.create_session_object(user)
      
@router.get("/auth/profile", status_code=status.HTTP_200_OK)
async def me(user : UserSession = Depends(auth_dependencies.auth_user)) -> UserSession:
    logger.info(f"[me] -> user: {user.email}")
    return user