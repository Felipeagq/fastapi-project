from passlib.context import CryptContext
from jose import jwt,JWTError
from fastapi.security import OAuth2PasswordBearer

from app.utils.settings import settings

from fastapi_login import LoginManager

manager = LoginManager(settings.SECRET_KEY,"/login")

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password(
    password:str
) -> str:
    return password_context.hash(password)