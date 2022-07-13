from fastapi import FastAPI
from app.routes.user_route import router as user_router
from app.routes.other_roter import router as other_router
from app.routes.files_router import router as file_rouer
from app.routes.streaming_file import router as stream_route
import uvicorn

from app.utils.settings import settings
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Demostración",
    version="v1.0.1"
)

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

app.include_router(
    stream_route,
    prefix="/video",
    tags=["stream Management"]
)




if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"]
    )


if __name__ == "__main__":
    uvicorn.run(
        "entrypoint:app",
        host="0.0.0.0",
        port=5000,
        workers=1,
        reload=True,
        # log_level= "debug",
        access_log=False,
        use_colors=True
    )