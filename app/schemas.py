from pydantic import BaseModel
from datetime import datetime


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
