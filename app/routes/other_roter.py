# Routes
from time import timezone
from fastapi import APIRouter, Depends

# Settings
from app.schemas import user_schema
from app.utils.security import get_current_user
from fastapi_utils.tasks import repeat_every
import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler
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


@router.get("/start1",)
@repeat_every(
    seconds=2,
    max_repetitions=15
)
def repeated_task_two() -> str:
    print("Imprimiendo 2")


@router.get("/start2")
async def other_repeater_task():
    scheduler = AsyncIOScheduler(timezone=pytz.utc)
    scheduler.start()
    # scheduler.add_job(some_task, "cron", hour=0)  # runs every night at midnight
    scheduler.add_job(
        some_task, 
        "interval", 
        seconds=3 # minutes, hours
        )  # runs every night at midnight
def some_task():
    print("impresion3")