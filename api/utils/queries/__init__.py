"""All query related utility functions."""
import requests
from flask import current_app
from api.types import UserInfo


def get_user_info(access_token: str) -> UserInfo:
    """Query Auth0 to get user information"""
    domain = current_app.config["AUTH0_DOMAIN"]
    return requests.get(
        f"https://{domain}/userinfo", {"access_token": access_token}, timeout=10
    ).json()
