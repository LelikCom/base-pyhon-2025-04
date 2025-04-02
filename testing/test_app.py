import pytest
from fastapi.testclient import TestClient
from app import app

@pytest.fixture
def test_client():
    return TestClient(app)

def test_index(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
