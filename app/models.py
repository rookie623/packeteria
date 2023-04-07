from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    lote = Column(String, nullable=False)
    turno = Column(String, nullable=False)
    es_retirado = Column(Boolean, server_default="FALSE", nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
