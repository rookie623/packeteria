import time
import psycopg2
from psycopg2.extras import RealDictCursor
from fastapi import FastAPI, Response, status, HTTPException
from post import Post
from random import randrange

app = FastAPI()
my_posts = [{"nombre": "Mariela", "apellido": "Chao", "turno": "mañana", "lote": 101,"retirado": False, "id": 1},
            {"nombre": "Gabriela", "apellido": "Sari", "turno": "tarde", "lote": 247,"retirado": False, "id": 2}]


while True:
    try:
        conn = psycopg2.connect(host="localhost", database="packeteria", user="postgres",
                                password="1mth3r00t", cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesfull!")
        break
    except Exception as error:
        print("Connecting to database failed!")
        print("Error: ", error)
        time.sleep(2)


def find_post_by_id(id):
    for p in my_posts:
        if p["id"] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i


@app.get("/")
def root():
    return {"message": "Welcome to Packetes API"}


@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM packetes """)
    packetes = cursor.fetchall()
    print(packetes)
    return {"data": packetes}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute("""INSERT INTO packetes (name, lastname, es_retirado, turno, lote)
                      VALUES (%s, %s, %s, %s, %s) RETURNING *""", (post.name, post.lastname, post.es_retirado, post.turno, post.lote))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}


@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute("""SELECT * FROM packetes WHERE id = %s """, (str(id),))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return {"post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute("""DELETE FROM packetes WHERE id = %s RETURNING *""", (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute("""UPDATE packetes SET name = %s, lastname = %s, es_retirado = %s, turno = %s, lote = %s WHERE id = %s RETURNING *""",
                   (post.name, post.lastname, post.es_retirado, post.turno, post.lote, str(id)))
    updated_post = cursor.fetchone()
    conn.commit()
    if updated_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")

    return {"data": updated_post}
