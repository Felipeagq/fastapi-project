from app.models.user_model import User
from app.db.postgres.pg_crud import PostgresDataBase
from app.utils.security import get_password

from fastapi import HTTPException

def create_user(
    user:str,
    db
):
    new_user = User(
        username= user.username,
        email=user.email,
        password= get_password(user.password),
        role = user.role
    )
    created_user = PostgresDataBase.create(
        db=db,
        entity=new_user
    )
    return created_user


def query_user(
    username:str,
    db
):
    queried_user = db.query(User).filter(User.username == username).first()
    if not queried_user:
        raise HTTPException(
            detail="user dont exits"
        )
    return queried_user