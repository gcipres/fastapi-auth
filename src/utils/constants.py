BCRYPT = "bcrypt"
ENCRYPT_ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 60 #60 minute token expiration
SECRET = "8dd4f2bad0d79244c6787e48a0d9a6e9a3f27db8a3baa8c867dec3e957e459dd" #generate in terminal (openssl rand -hex 32)    

JWT_INVALID = "Invalid token"
JWT_EXPIRED = "Session expired"

USER_ALREADY_EXIST = "The user already exist in the system"
USER_DOES_NOT_EXIST = "The user does not exist in the system"
PASSWORD_INCORRECT = "Password incorrect"