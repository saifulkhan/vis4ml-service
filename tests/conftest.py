"""
Pytest configuration and fixtures.

This module provides shared test fixtures and configuration
for all tests in the project.
"""
import pytest
from fastapi.testclient import TestClient

from main import create_app


@pytest.fixture
def app():
    """
    Create a FastAPI application instance for testing.

    Returns:
        FastAPI: Application instance
    """
    return create_app()


@pytest.fixture
def client(app):
    """
    Create a test client for the FastAPI application.

    Args:
        app: FastAPI application fixture

    Returns:
        TestClient: Test client instance
    """
    return TestClient(app)
