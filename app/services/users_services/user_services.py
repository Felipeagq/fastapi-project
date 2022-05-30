from app.models.user_model import User
from app.db.postgres.pg_crud import PostgresDataBase
from app.utils.security import get_password


def create_user(
    user,
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