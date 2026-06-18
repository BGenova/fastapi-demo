from fastapi import FastAPI, UploadFile
from app.routers import users

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
