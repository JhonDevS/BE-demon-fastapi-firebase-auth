import json

import pyrebase
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials
from firebase_admin.auth import verify_id_token
from typing import Annotated, Optional

from service.config_firebase import bearer_scheme

firebase = pyrebase.initialize_app(json.load(open('firebase_config.json')))


def verify_user_token(
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


def login(email: str, password: str):
    try:
        user = firebase.auth().sign_in_with_email_and_password(email, password)
        return user['idToken']
    except Exception:
        raise HTTPException(detail={'message': 'There was an error logging in'}, status_code=400)
