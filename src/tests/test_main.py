# pyrefly: ignore [missing-import]
from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)

def test_read_healthcheck():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"message": "Alive", "data": {"test": "only to validate"}}
