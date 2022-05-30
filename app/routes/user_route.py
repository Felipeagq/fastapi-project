# Routes
from urllib import request
from fastapi_utils.cbv import cbv
from fastapi import APIRouter, Depends, status, Request

#db
from sqlalchemy.orm import Session
from app.db.postgres.pg_core import get_db
from app.models.user_model import User
from app.db.postgres.pg_crud import PostgresDataBase

# Schemas
from app.schemas import user_schema

# Services
from app.services.users_services import user_services 

# Security
from fastapi.security import OAuth2PasswordRequestForm
from app.utils.security import is_valid,created_access_token

router = APIRouter()

@cbv(router)
class UserRoute:
    db:Session = Depends(get_db)
    request: Request

    @router.post(
        "/",
        status_code= status.HTTP_202_ACCEPTED,
    )
    def create_user(
        self, 
        user: user_schema.UserRequestSchema
    ):
        created_user = user_services.create_user(
            user,
            self.db
        )
        return created_user        


    @router.post('/login')
    def login(self,data: OAuth2PasswordRequestForm = Depends()):
        username = data.username
        password = data.password
        user = user_services.query_user(username,db=self.db)
        if not user:
            raise "error"
        elif not is_valid(password,user.password):
            raise "error"
        access_token = created_access_token(username)

        return {'access_token': access_token}