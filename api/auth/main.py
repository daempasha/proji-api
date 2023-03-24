"""All auth related functions"""

import os

from authlib.integrations.flask_oauth2 import ResourceProtector
from authlib.oauth2 import OAuth2Error
from authlib.oauth2.rfc6749.errors import (
    MissingAuthorizationError,
    InvalidScopeError,
)
from authlib.oauth2.rfc6750.errors import InvalidTokenError

from .validator import Auth0JWTBearerTokenValidator


class AlteredResourceProtector(ResourceProtector):
    """
    A modified version of the `ResourceProtector` class
    that overrides the `raise_error_response` method.

    Methods:
    --------
    raise_error_response(error: OAuth2Error) -> Response:
        Override the `raise_error_response` method to
        provide custom error handling for certain types of errors.

    """

    def raise_error_response(self, error: OAuth2Error):
        """Override the `raise_error_response` method since errorhandler
        wasn't catching these raised errors."""
        error_code = error.error

        if error_code == "missing_authorization":
            raise MissingAuthorizationError()

        if error_code == "insufficient_scope":
            raise InvalidScopeError()

        if error_code == "invalid_token_error":
            raise InvalidTokenError()

        return super().raise_error_response(error)


require_auth = AlteredResourceProtector()
validator = Auth0JWTBearerTokenValidator(
    os.environ["AUTH0_DOMAIN"], os.environ["AUTH0_AUDIENCE"]
)
require_auth.register_token_validator(validator)
