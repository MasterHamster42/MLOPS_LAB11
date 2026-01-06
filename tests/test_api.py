import pytest
from fastapi.testclient import TestClient

from src.sentiment_app.app import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
