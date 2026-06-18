from fastapi import FastAPI, UploadFile
import httpx
from mistralai.client import Mistral
from app.routers import users
from app.core.config import settings

app = FastAPI(title="FastAPI Demo")


app.include_router(
    users.router,
    prefix="/users",
    tags=["users"]
)

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/upload")
async def upload(
    file: UploadFile
):
    content = await file.read()

    return {
        "filename": file.filename,
        "size": len(content)
    }

@app.get("/async")
async def test_async():
    return {"ok": True}

@app.get("/weather")
async def weather():
    async with httpx.AsyncClient() as client:
        # Note: api.example.com est un placeholder, on s'attend à ce que ça puisse échouer ou être simulé
        response = await client.get(
            "https://api.example.com"
        )
    return response.json()

@app.post("/chat")
def chat(prompt: str):
    client = Mistral(api_key=settings.MISTRAL_API_KEY)
    response = client.chat.complete(
        model="mistral-large-latest",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return {
        "answer":
        response.choices[0]
        .message
        .content
    }
