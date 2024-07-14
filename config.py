import os
import pathlib
from functools import lru_cache
from typing import Annotated, Optional

from dotenv import load_dotenv
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from firebase_admin.auth import verify_id_token
from pydantic_settings import BaseSettings

# firebase handler errors
bearer_scheme = HTTPBearer(auto_error=False)

basedir = pathlib.Path(__file__).parents[1]
completed_dir = basedir / "demo-fastapi-firebase-auth/.env"
load_dotenv(completed_dir)


class Settings(BaseSettings):
    app_name: str = "demo-fastapi-firebase-auth"
    env: str = os.getenv("ENV", "development")
    frontend_url: str = os.getenv("FRONTEND_URL", "NA")
    credential_fire_base: str = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")


@lru_cache
def get_settings() -> Settings:
    """Retrieves the fastapi settings"""
    return Settings()


def get_firebase_user_from_token(
        token: Annotated[Optional[HTTPAuthorizationCredentials], Depends(bearer_scheme)],
) -> Optional[dict]:
    try:
        print(token)
        if not token:
            raise ValueError("No token")
        user = verify_id_token(token.credentials)
        return user
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not logged in or Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
