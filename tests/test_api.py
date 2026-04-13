from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    # Accept both "healthy" (with DB) and "degraded" (without DB in CI)
    assert data["status"] in ["healthy", "degraded"]

def test_homepage():
    response = client.get("/")
    assert response.status_code == 200