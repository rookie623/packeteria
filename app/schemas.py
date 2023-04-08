from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class PostBase(BaseModel):
    name: str
    lastname: str
    lote: str
    turno: str
    es_retirado: bool = False


class CreatePost(PostBase):
    pass


class UpdatePost(PostBase):
    pass


class ResponsePost(PostBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    password: str


class CreateUser(UserBase):
    pass


class ResponseUser(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class UserOut(BaseModel):
    id: int
    username: str
    created_at: datetime

    class Config:
        orm_mode = True


class ResponsePassword(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


class UpdatePassword(BaseModel):
    password: str


class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None
