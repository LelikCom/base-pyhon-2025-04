# testing/test_app.py
import pytest
from fastapi.testclient import TestClient
from app import app

@pytest.fixture
def client():
    return TestClient(app)

def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
