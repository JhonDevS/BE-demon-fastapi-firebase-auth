from fastapi import FastAPI
from router import auth_routes
from fastapi.middleware.cors import CORSMiddleware
from config import get_settings
from service.config_firebase import init_service

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
init_service()

