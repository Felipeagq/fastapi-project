from fastapi import FastAPI
from app.routes.user_route import router as user_router
from app.routes.other_roter import router as other_router
from app.routes.files_router import router as file_rouer

from app.utils.settings import settings
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(
    user_router,
    prefix="/user",
    tags=["User Management"]
)


app.include_router(
    other_router,
    prefix="/other",
    tags=["task Management"]
)

app.include_router(
    file_rouer,
    prefix="/file",
    tags=["file Management"]
)



if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"]
    )