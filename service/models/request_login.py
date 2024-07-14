from pydantic import BaseModel


class RequestLogin(BaseModel):
    email: str
    password: str
