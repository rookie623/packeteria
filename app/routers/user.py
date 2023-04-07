from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, utils
from .. database import get_db

router = APIRouter(
    tags=["Users"]
)


@router.get("/users", response_model=List[schemas.ResponseUser])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    hashed_password = utils.hasher(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
