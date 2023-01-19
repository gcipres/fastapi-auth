import logging
from datetime import datetime
from uuid import UUID
from src.users import crud as users_crud
from src.users.schemas import User
from src.utils import encrypt, generate_password

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s -%(name)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

def create_user(user: User) -> User:
    logger.info(f"[create_user] -> {user.email}")
    password = generate_password.generate_password()
    user.password = encrypt.crypt.encrypt(password)
    user.create_at = datetime.now().timestamp()

    user_db = users_crud.create_user(user)
    user_created: User = User(**{col:val for col, val in user_db.items()})
    print("THIS IS YOUR PASSWORD, PRINT ONLY FOR TEST, YOU NEED SEND BY EMAIL TO THE USER WITH A EMAIL SENDER SERVICE OR REQUEST IN PETITION")
    print("*************************")
    print(password)
    print("*************************")
    user_created.password = None
    
    return user_created

def get_user(email: str) -> User | None:
    logger.info(f"[get_user] -> {email}")
    user_db = users_crud.get_user(email)

    if user_db is None:
        return None

    return User(**{col:val for col, val in user_db.items()})

def check_email(email: str) -> bool:
    user = get_user(email)
    return True if user else False