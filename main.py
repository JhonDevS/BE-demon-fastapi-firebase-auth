from fastapi import FastAPI
from router import auth_routes
# pip install firebase-admin
import firebase_admin
from firebase_admin import credentials
from fastapi.middleware.cors import CORSMiddleware
from config import get_settings
import os

app = FastAPI()
app.include_router(auth_routes.router)

origins = [get_settings().frontend_url, "http://192.168.1.58:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cred = credentials.Certificate(get_settings().credential_fire_base)
firebase_admin.initialize_app(cred)
