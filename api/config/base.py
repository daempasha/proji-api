"""Basic configuration for all environments to inherit"""
import os


class Base:
    """Base configuration class"""

    DEBUG = False
    FRONTEND_HOST = "http://localhost:5173"

    MONGO_URI = os.environ["MONGO_URI"]

    AUTH0_CLIENT_ORIGIN_URL=os.environ.get("AUTH0_CLIENT_ORIGIN_URL")
    AUTH0_AUDIENCE=os.environ.get("AUTH0_AUDIENCE")
    AUTH0_DOMAIN=os.environ.get("AUTH0_DOMAIN")
