"""
health check endpoints.
"""

from fastapi import APIRouter

from app.core.config import config

router = APIRouter(tags=["Health"])


@router.get("/health")
async def health_check():
    """
    health check endpoint.

    returns the current status of the application, useful for
    load balancers, container orchestration, and monitoring.

    returns:
        dict: Health status information including:
            - status: Current health status
            - version: Application version
            - environment: Current environment (development, staging, production)

    example:
        ```json
        {
            "status": "healthy",
            "version": "0.1.0",
            "environment": "development"
        }
        ```
    """
    return {"status": "healthy", "version": "0.1.0", "environment": config.ENVIRONMENT}
