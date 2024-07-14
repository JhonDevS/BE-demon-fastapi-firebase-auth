import os
import pathlib
from functools import lru_cache
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

basedir = pathlib.Path(__file__).parents[1]
completed_dir = basedir / "demo-fastapi-firebase-auth/.env"
load_dotenv(completed_dir)


class Settings(BaseSettings):
    app_name: str = "demo-fastapi-firebase-auth"
    env: str = os.getenv("ENV", "development")
    frontend_url: str = os.getenv("FRONTEND_URL", "NA")
    credential_fire_base: str = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    print("creando la clase")


@lru_cache
def get_settings() -> Settings:
    """Retrieves the fastapi settings"""
    return Settings()
