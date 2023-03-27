"""Basic configuration for all environments to inherit"""
import os

class Base:
    """Base configuration class"""

    FRONTEND_HOST = "http://localhost:5173"
    AUTH0_API_KEY = "API_KEY"
    DEBUG = 0

    SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]