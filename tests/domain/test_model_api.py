"""
Tests for Model API endpoints.
"""
from fastapi.testclient import TestClient

from app.core.config import config


def test_model_hello_world(client: TestClient):
    """Test model domain hello world endpoint"""
    response = client.get(f"{config.api_base_path}/model/hello")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Hello World from Model API"
    assert data["status"] == "success"


def test_model_hello_world_headers(client: TestClient):
    """Test model domain endpoint returns correlation ID"""
    response = client.get(f"{config.api_base_path}/model/hello")
    assert "x-correlation-id" in response.headers
    assert "x-process-time" in response.headers
