import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = "FastAPI Demo"
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///./db.sqlite"
    )
    SECRET_KEY = os.getenv("SECRET_KEY", "secret")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

settings = Settings()