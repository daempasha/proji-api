"""All error classes."""


class ApiError(Exception):
    """Base exception for all Proji API errors."""

    status_code = 500
    message = "Internal server error"

    def __init__(self, message: str = None) -> None:
        if message:
            self.message = message

        super().__init__(message)

    def to_dict(self):
        """Convert error to dictionary."""
        return {"message": self.message}, self.status_code


class ValidationError(ApiError):
    """Exception to raise when arguments could not be validated."""

    status_code = 422
    message = "Could not validate all arguments."
