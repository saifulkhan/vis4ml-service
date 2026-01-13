from typing import Any, Optional

from pydantic import BaseModel


class ErrorResponse(BaseModel):
    """
    standard error response model.

    attributes:
        error_code: machine-readable error code
        message: human-readable error message
        details: optional additional error details
        correlation_id: request correlation ID for tracing
    """

    error_code: str
    message: str
    details: Optional[dict[str, Any]] = None
    correlation_id: Optional[str] = None


class CustomException(Exception):
    """
    base custom exception for the application.

    all custom exceptions should inherit from this class to ensure
    consistent error handling across the application.

    attributes:
        code: http status code
        error_code: machine-readable error code
        message: human-readable error message
        details: optional additional error details
    """

    def __init__(
        self,
        code: int,
        error_code: str,
        message: str,
        details: Optional[dict[str, Any]] = None,
    ):
        self.code = code
        self.error_code = error_code
        self.message = message
        self.details = details
        super().__init__(self.message)


class NotFoundException(CustomException):
    """raised when a requested resource is not found"""

    def __init__(
        self,
        message: str = "Resource not found",
        details: Optional[dict[str, Any]] = None,
    ):
        super().__init__(
            code=404, error_code="NOT_FOUND", message=message, details=details
        )


class BadRequestException(CustomException):
    """raised when the request is invalid"""

    def __init__(
        self, message: str = "Bad request", details: Optional[dict[str, Any]] = None
    ):
        super().__init__(
            code=400, error_code="BAD_REQUEST", message=message, details=details
        )


class UnauthorizedException(CustomException):
    """raised when authentication is required but missing or invalid"""

    def __init__(
        self, message: str = "Unauthorized", details: Optional[dict[str, Any]] = None
    ):
        super().__init__(
            code=401, error_code="UNAUTHORIZED", message=message, details=details
        )


class ForbiddenException(CustomException):
    """raised when the user doesn't have permission to access a resource"""

    def __init__(
        self, message: str = "Forbidden", details: Optional[dict[str, Any]] = None
    ):
        super().__init__(
            code=403, error_code="FORBIDDEN", message=message, details=details
        )


class InternalServerException(CustomException):
    """raised when an internal server error occurs"""

    def __init__(
        self,
        message: str = "Internal server error",
        details: Optional[dict[str, Any]] = None,
    ):
        super().__init__(
            code=500,
            error_code="INTERNAL_SERVER_ERROR",
            message=message,
            details=details,
        )
