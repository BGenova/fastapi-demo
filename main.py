from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr
    age: int

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Jane"}
    ]

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id}

@app.get("/search")
def search(q: str):
    return {"query": q}

@app.post("/users")
def create_user(user: User):
    return user