from fastapi import APIRouter, Depends
from app.schemas import user_schema
from app.utils.security import get_current_user

from fastapi_utils.tasks import repeat_every

router = APIRouter()

@router.get("/")
def retorno(
    get_current_user:user_schema.UserRequestSchema = Depends(get_current_user)
):
    return  get_current_user



@router.on_event("startup")
@repeat_every(seconds=60)
def repeated_task() -> str:
    """
    Internal Task that start on the startup event.
    Must dont have arguments.
    Repeat every "n" seconds
    """
    print("imprimiendo")