from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/blog")
def home(limit: int = 10, published: bool = False, sort: Optional[bool] = None):
    # only get 10 published blog
    if published:
        return {"data": f"{limit} published blogs from database"}
    return {"data": f"{limit}  blogs from database"}

@app.get('/blog/unpublished')
def unpublihsed():
    return {'data': 'all unpublished blog'}


@app.get("/blog/{id}")
def show(id: int):
    return {"page": f"Get Blog {id}"}


@app.get("/blog/{id}/comments")
def get_comments(id: int):
    return {"page": f"Get Blog {id} with comments"}

class Blog(BaseModel):
    title: str
    description: str
    published: Optional[bool]

@app.post("/blog")
def create_blog(blog: Blog):
    return {'data': {"title": blog.title, "description": blog.description, "published": blog.published}}