from ..database import connection
from uuid import UUID
from src.users.models import UserDB
from src.users.schemas import User

def create_user(user: User):
    return connection.execute(
        UserDB
        .insert()
        .values(user.dict())
    ).last_inserted_params()

def get_user(email: str):
    return connection.execute(
        UserDB
        .select()
        .where(UserDB.c.email == email)
    ).first()