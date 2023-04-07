from fastapi import FastAPI, Response, status, HTTPException, Depends
from app.post import Post
from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to Packetes API"}


@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    packetes = db.query(models.Post).all()
    return {"data": packetes}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post, db: Session = Depends(get_db)):
    new_post = models.Post(**post.dict())
    print(new_post)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data": new_post}


@app.get("/posts/{post_id}")
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {post_id} was not found")
    return {"post_detail": post}


@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    deleted_post = db.query(models.Post).filter(models.Post.id == post_id)
    if deleted_post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {post_id} does not exist")

    deleted_post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{post_id}")
def update_post(post_id: int, updated_post: Post, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == post_id)
    post = post_query.first()

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {post_id} does not exist")

    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return {"data": post_query.first()}
