from app.schemas.user import UserCreate

# Simulation base mémoire (plus tard remplacé par DB)
fake_db = []
current_id = 1


def get_users():
    return fake_db


def create_user(user: UserCreate):
    global current_id

    new_user = {
        "id": current_id,
        "name": user.name,
        "email": user.email
    }

    fake_db.append(new_user)
    current_id += 1

    return new_user
