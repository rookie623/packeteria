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


@router.get("/users/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {user_id} was not found")
    return user


@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted_user = db.query(models.User).filter(models.User.id == user_id)
    if deleted_user.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {user_id} does not exist")
    deleted_user.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/users/{user_id}", response_model=schemas.ResponsePassword)
def update_password_user(user_id: int, updated_user: schemas.UserBase, db: Session = Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.id == user_id)
    user = user_query.first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {user_id} does not exist")
    user_query.update(updated_user.dict(), synchronize_session=False)
    db.commit()
    return user_query.first()
