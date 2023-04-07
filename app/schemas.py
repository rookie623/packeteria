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
