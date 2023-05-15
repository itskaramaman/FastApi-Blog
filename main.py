from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"page": "Home Page"}