from pydantic import BaseModel


class Post(BaseModel):
    name: str
    lastname: str
    es_retirado: bool
    turno: str
    lote: int

    """def __init__(self, nombre, apellido, turno):
        self.nombre = nombre
        self.apellido = apellido
        self.turno = turno
    """