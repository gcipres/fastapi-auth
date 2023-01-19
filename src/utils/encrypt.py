from passlib.context import CryptContext
from ..utils import constants

crypt = CryptContext(schemes=[constants.BCRYPT])