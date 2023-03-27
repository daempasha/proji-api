"""Application related functions"""
import os
from flask import Flask


def get_config_path(app: Flask) -> str:
    """Returns the path of the most appropriate
    configuration based on environment and app settings."""

    debug = app.config["DEBUG"]
    testing = os.environ.get("TESTING", default="0") == "1"

    if testing:
        config = "api.config.Testing"
    elif debug:
        config = "api.config.Development"
    else:
        config = "api.config.Production"

    return config
