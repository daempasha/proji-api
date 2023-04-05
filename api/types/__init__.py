"""Defining all types that might be needed. Will start off as a single __init__
but might move to separate  if there are too many"""
from typing import TypedDict


class UserInfo(TypedDict):
    """User info retrieved from Auth0 /userinfo endpoint"""

    sub: str
    email: str
    email_verified: bool
    picture: str
    locale: str
