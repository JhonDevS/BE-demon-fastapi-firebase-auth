from fastapi import APIRouter, Depends
from typing import Annotated
from starlette.responses import JSONResponse
from service.firebase import verify_user_token, login, signup, sign_out
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


@router.post("/signup", include_in_schema=False)
async def post_creation_user(request: RequestLogin):
    email = request.email
    password = request.password
    jwt = signup(email, password)
    return JSONResponse(content={'token': jwt}, status_code=200)


# router de sing out
@router.post("/sign-out")
async def post_sign_out(user: Annotated[dict, Depends(verify_user_token)]):
    user_id = user['uid']
    if not user_id:
        return JSONResponse(content={'message': 'No valid token'}, status=400)
    sign_out(user_id)
    return JSONResponse(content={'message': 'Successfully signed out'}, status_code=200)
