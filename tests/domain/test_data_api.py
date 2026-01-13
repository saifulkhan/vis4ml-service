"""
Tests for Data API endpoints.
"""
from fastapi.testclient import TestClient

from app.core.config import config


def test_data_hello_world(client: TestClient):
    """Test data domain hello world endpoint"""
    response = client.get(f"{config.api_base_path}/data/hello")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Hello World from Data API"
    assert data["status"] == "success"


def test_data_hello_world_headers(client: TestClient):
    """Test data domain endpoint returns correlation ID"""
    response = client.get(f"{config.api_base_path}/data/hello")
    assert "x-correlation-id" in response.headers
    assert "x-process-time" in response.headers
