from fastapi.security import HTTPBearer
# pip install firebase-admin
import firebase_admin
from firebase_admin import credentials
from config import get_settings

# firebase handler errors
bearer_scheme = HTTPBearer(auto_error=False)


def init_service():
    cred = credentials.Certificate(get_settings().credential_fire_base)
    firebase_admin.initialize_app(cred)
    print("Firebase initialized", firebase_admin.get_app())
