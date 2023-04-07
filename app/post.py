from pydantic import BaseModel


class Post(BaseModel):
    name: str
    lastname: str
    turno: str
    es_retirado: bool = False
    lote: int
