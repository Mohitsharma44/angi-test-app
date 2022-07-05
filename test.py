from fastapi.testclient import TestClient

from main import app, VERSION

client = TestClient(app)


def test_healthz():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}

def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Version": VERSION}
