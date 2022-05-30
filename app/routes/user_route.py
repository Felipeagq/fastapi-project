from urllib import request
from fastapi_utils.cbv import cbv
from fastapi import APIRouter, Depends, status, Request

from sqlalchemy.orm import Session
from app.db.postgres.pg_core import get_db
from app.models.user_model import User

from app.schemas import user_schema
from app.db.postgres.pg_crud import PostgresDataBase
from app.services.users_services import user_services 

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
    