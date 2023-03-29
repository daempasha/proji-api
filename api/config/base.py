"""Basic configuration for all environments to inherit"""
import os


class Base:
    """Base configuration class"""

    DEBUG = False
    FRONTEND_HOST = "http://localhost:5173"
    AUTH0_API_KEY = "API_KEY"

    MONGO_URI = os.environ["MONGO_URI"]
