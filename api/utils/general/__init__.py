"""General utility functions."""
from flask import request


def extract_access_token():
    """Extract access token from header"""
    return request.headers["Authorization"].split(" ")[1]
