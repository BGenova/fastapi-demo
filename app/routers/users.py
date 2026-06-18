from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.schemas.user import UserCreate, UserOut
from app.services.user_service import create_user, get_users
from app.core.security import create_access_token, decode_access_token

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Simulation de vérification (on accepte tout pour l'exemple)
    if form_data.username == "admin" and form_data.password == "password":
        access_token = create_access_token(data={"sub": form_data.username})
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password"
    )

@router.get("/profile")
def profile(current_user=Depends(get_current_user)):
    return current_user

@router.get("/", response_model=list[UserOut])
def list_users():
    return get_users()

@router.post("/", response_model=UserOut)
def add_user(user: UserCreate):
    return create_user(user)
