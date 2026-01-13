"""
VIS4ML4HD Main Application.

Visualization for Machine Learning to Support Human-Centered Decision Making.
This is the main entry point for the FastAPI application.
"""

from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app import get_available_domain_routers
from app.core.config import config
from app.core.exceptions import CustomException, ErrorResponse
from app.core.health import router as health_router
from app.core.logging import logger, setup_logger
from app.core.middleware import RequestLoggingMiddleware


def init_routers(app_: FastAPI) -> None:
    """
    initialize all application routers.

    includes health check and dynamically discovered domain routers.

    Args:
        app_: FastAPI application instance
    """
    # Add health check endpoint (no versioning)
    app_.include_router(health_router)

    # Add all domain routers with versioning
    routers = get_available_domain_routers()
    for router in routers:
        app_.include_router(router, prefix=config.api_base_path)


@asynccontextmanager
async def lifespan_handler(app_: FastAPI):
    """
    Application lifespan handler for startup and shutdown events.

    Args:
        app_: FastAPI application instance
    """
    # Startup
    app_.state.logger = setup_logger(log_level=config.LOG_LEVEL)
    logger.info(f"Application starting in {config.ENVIRONMENT} environment")
    logger.info(f"API base path: {config.api_base_path}")

    yield

    # Shutdown
    logger.info("Application shutting down")


def init_middleware(app_: FastAPI) -> None:
    """
    Initialize application middleware.

    Configures CORS and request logging middleware.

    Args:
        app_: FastAPI application instance
    """
    # CORS middleware
    app_.add_middleware(
        CORSMiddleware,
        allow_origins=config.cors_origins_list,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Request logging middleware
    app_.add_middleware(RequestLoggingMiddleware)


def init_exception_handlers(app_: FastAPI) -> None:
    """
    initialize exception handlers for the application.
    provides consistent error responses across the application.

    args:
        app_: fastapi application instance
    """

    @app_.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        """handle custom application exceptions"""

        correlation_id = getattr(request.state, "correlation_id", None)

        error_response = ErrorResponse(
            error_code=exc.error_code,
            message=exc.message,
            details=exc.details,
            correlation_id=correlation_id,
        )

        logger.error(
            f"[{correlation_id}] CustomException: {exc.error_code} - {exc.message}"
        )

        return JSONResponse(
            status_code=exc.code,
            content=error_response.model_dump(exclude_none=True),
        )

    @app_.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        """handle unexpected exceptions"""

        correlation_id = getattr(request.state, "correlation_id", None)

        logger.exception(f"[{correlation_id}] unhandled exception: {str(exc)}")

        error_response = ErrorResponse(
            error_code="INTERNAL_SERVER_ERROR",
            message="an unexpected error occurred",
            correlation_id=correlation_id,
        )

        return JSONResponse(
            status_code=500,
            content=error_response.model_dump(exclude_none=True),
        )


def create_app() -> FastAPI:
    """
    create and configure the fastapi application.

    returns:
        fastapi: configured application instance
    """
    app_ = FastAPI(
        title="vis4ml",
        description="vis4ml api",
        version="0.1.0",
        docs_url=None if config.is_production else "/docs",
        redoc_url=None if config.is_production else "/redoc",
        lifespan=lifespan_handler,
    )

    # Initialize components
    init_middleware(app_)
    init_routers(app_)
    init_exception_handlers(app_)

    return app_


app = create_app()


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=config.HOST,
        port=config.PORT,
        reload=not config.is_production,
        workers=1,
    )
