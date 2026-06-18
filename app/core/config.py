import os

class Settings:
    APP_NAME = "FastAPI Demo"
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///./db.sqlite"
    )
    SECRET_KEY = os.getenv("SECRET_KEY", "secret")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

settings = Settings()