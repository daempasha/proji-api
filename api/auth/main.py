"""All auth related functions"""

import os
from authlib.integrations.flask_oauth2 import ResourceProtector
from .validator import Auth0JWTBearerTokenValidator

require_auth = ResourceProtector()
validator = Auth0JWTBearerTokenValidator(
    os.environ["AUTH0_DOMAIN"], os.environ["AUTH0_AUDIENCE"]
)
require_auth.register_token_validator(validator)
