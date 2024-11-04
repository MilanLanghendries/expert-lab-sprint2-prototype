from app import create_app
import pytest

@pytest.fixturepip
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200

def test_random_message(client):
    response = client.get("/api/message")
    assert response.status_code == 200
    assert "message" in response.get_json()
