from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .schemas import Blog
from .models import Base, Blog as BlogModel
from .database import engine, SessionLocal

app = FastAPI()

Base.metadata.create_all(engine)  

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/blog")
def create_blog(request: Blog, session: Session = Depends(get_db)):
    blog = BlogModel(title=request.title, body=request.body)
    session.add(blog)
    session.commit()
    session.refresh(blog)
    return blog


@app.get("/blog")
def get_blogs(session: Session = Depends(get_db)):
    blogs = session.query(BlogModel).all()
    return blogs

@app.get("/blog/{blog_id}")
def get_blog(id: int, session: Session = Depends(get_db)):
    blog = session.query(BlogModel).filter(BlogModel.id==id).first()
    return blog


