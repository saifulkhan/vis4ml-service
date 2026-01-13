import time
import uuid
from collections.abc import Callable

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.logging import logger


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """
    middleware to log http requests and responses.

    adds correlation ID to each request for tracing.
    logs request method, path, processing time, and status code.
    """

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # generate correlation ID for request tracing
        correlation_id = str(uuid.uuid4())
        request.state.correlation_id = correlation_id

        # start timer
        start_time = time.time()

        # log incoming request
        logger.info(
            f"[{correlation_id}] Incoming request: {request.method} {request.url.path}"
        )

        # process request
        try:
            response = await call_next(request)
        except Exception as e:
            # log error
            process_time = time.time() - start_time
            logger.error(
                f"[{correlation_id}] Request failed: {request.method} {request.url.path} "
                f"- Error: {str(e)} - Duration: {process_time:.3f}s"
            )
            raise

        # calculate processing time
        process_time = time.time() - start_time

        # add headers
        response.headers["X-Correlation-ID"] = correlation_id
        response.headers["X-Process-Time"] = f"{process_time:.3f}"

        # log response
        logger.info(
            f"[{correlation_id}] Completed: {request.method} {request.url.path} "
            f"- Status: {response.status_code} - Duration: {process_time:.3f}s"
        )

        return response
