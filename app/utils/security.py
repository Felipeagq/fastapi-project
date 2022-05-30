# Routes
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException,status

# Security
from passlib.context import CryptContext
from jose import jwt,JWTError

# Settings
from app.utils.settings import settings
from typing import Union,Any
from datetime import datetime,timedelta
from app.schemas.token_schemas import TokenData
from app.schemas.user_schema import UserResponseSchema

# db
from sqlalchemy.orm import Session
from app.db.postgres.pg_core import get_db
from app.services.users_services import user_services

oauth2_scheme = OAuth2PasswordBearer( tokenUrl="/user/login" )

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def created_access_token(
    subject:str,
    expire_delta: timedelta = None
) -> str :
    print("....",subject)
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
            )
    to_encode ={
        "sub": subject,
        "exp": expire
    }
    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )



def get_password(
    password:str
) -> str:
    return password_context.hash(password)


def is_valid(
    plain_password:str,
    hashed_password:str
) -> str:
    return password_context.verify(
        plain_password,
        hashed_password
    )



def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate":"Bearer"}
    )
    
    try: 
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        subjet = payload.get("sub")
        # token_data= TokenData(username=subjet,role=role)
    except Exception as e:
        print(e)
        return e
    
    user = user_services.query_user(subjet,db)
    if not user:
        raise credentials_exception
    # if token_data is None:
    #     raise credentials_exception
    
    return UserResponseSchema(
        username= user.username,
        email=user.email,
        role=user.role
    )