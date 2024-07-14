from fastapi import APIRouter, Depends
from typing import Annotated
from starlette.responses import JSONResponse
from service.firebase import verify_user_token, login
from service.models.request_login import RequestLogin

router = APIRouter()


@router.get("/verify-token")
async def get_userid(user: Annotated[dict, Depends(verify_user_token)]):
    """gets the firebase connected user"""
    return {"id": user["uid"]}


@router.post("/login", include_in_schema=False)
async def post_login(request: RequestLogin):
    email = request.email
    password = request.password
    jwt = login(email, password)
    return JSONResponse(content={'token': jwt}, status_code=200)
