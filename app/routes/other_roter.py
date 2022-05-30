from fastapi import APIRouter, Depends
from app.schemas import user_schema
from app.utils.security import get_current_user


router = APIRouter()

@router.get("/")
def retorno(
    get_current_user:user_schema.UserRequestSchema = Depends(get_current_user)
):
    print(get_current_user)
    return  get_current_user