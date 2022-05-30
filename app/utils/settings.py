import os 
from dotenv import load_dotenv
from typing import Any, List,Optional, Union
from pydantic import BaseSettings,AnyHttpUrl


import logging

load_dotenv()

class Settings(BaseSettings):

    # LOGS
    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(
        filename="./logs",
        level=logging.INFO,
        format=LOG_FORMAT,
        filemode="a"
    )
    @staticmethod
    async def log(request,response):
        import json
        body = None
        await request.body()
        if request._body:
            body = json.loads(request._body)
        _log = {
        "path":request.url._url,
        "request": body,
        "response":response
    }
        logging.info(_log)
    
    # PROJECT INFO
    PROJECT_NAME:str = "Big Study"
    PROJECT_VERSION:str = "v0.0.0"
    API_V1_STR:str = "/api/v1"
    
    # SECURITY UTILS
    SECRET_KEY: str = "5126402477d3baacae24c2be"
    # SECRET_KEY: str = os.getenv("SECRET_KEY") or os.urandom(12).hex()
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("TOKEN_EXPIRE_MINUTES") or 60
    ALGORITHM: str = "HS256"
    
    # POSTGRES GENERAL CREDENTIALS
    _PG_NAME: str = os.getenv("PG_NAME") or None
    _PG_USER: str = os.getenv("PG_USER") or None
    _PG_PASSWORD: str = os.getenv("PG_PASSWORD") or None
    _PG_HOST: str = os.getenv("PG_HOST") or None
    _PG_PORT:str = os.getenv("PG_PORT") or None

    # POSTGRES DATABASE URL CONSTRUCTION
    SQLALCHEMY_DATABASE_URL: str = f"postgresql://{_PG_USER}:{_PG_PASSWORD}@{_PG_HOST}:{_PG_PORT}"
    
    # CORS
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []


settings = Settings()
