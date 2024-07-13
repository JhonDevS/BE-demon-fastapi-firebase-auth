from fastapi import FastAPI
from router import auth_routes
# pip install firebase-admin
import firebase_admin
from fastapi.middleware.cors import CORSMiddleware
from config import get_settings

app = FastAPI()
app.include_router(auth_routes.router)

origins = [get_settings().frontend_url]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

firebase_admin.initialize_app()
print("Current App Name:", firebase_admin.get_app().project_id)
