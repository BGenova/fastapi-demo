from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_protected_route_without_token():
    # Test d'accès à une route protégée sans token
    response = client.get("/users/profile")
    assert response.status_code == 401
    print("Accès refusé sans token : OK")

def test_login_and_access_protected_route():
    # 1. Tentative de login
    login_data = {"username": "admin", "password": "password"}
    response = client.post("/users/login", data=login_data)
    assert response.status_code == 200
    token = response.json()["access_token"]
    print(f"Login réussi, token récupéré : {token[:20]}...")

    # 2. Accès à la route protégée avec le token
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/users/profile", headers=headers)
    assert response.status_code == 200
    assert response.json()["sub"] == "admin"
    print("Accès autorisé avec token valide : OK")

def test_invalid_token():
    headers = {"Authorization": "Bearer invalid-token"}
    response = client.get("/users/profile", headers=headers)
    assert response.status_code == 401
    print("Accès refusé avec token invalide : OK")

if __name__ == "__main__":
    print("--- Démarrage des tests API ---")
    try:
        test_protected_route_without_token()
        test_login_and_access_protected_route()
        test_invalid_token()
        print("--- Tous les tests ont réussi ! ---")
    except Exception as e:
        print(f"--- Échec des tests : {e} ---")
