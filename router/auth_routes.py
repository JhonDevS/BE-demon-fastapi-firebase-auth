from fastapi import APIRouter, Depends
from typing import Annotated
from service.firebase import get_firebase_user_from_token

router = APIRouter()


@router.get("/userid")
async def get_userid(user: Annotated[dict, Depends(get_firebase_user_from_token)]):
    """gets the firebase connected user"""
    return {"id": user["uid"]}
