"""Contains all the error_handlers exports such as the 
register_error_handlers method and also all custom exception classes."""

from flask import Flask, jsonify
from authlib.oauth2.rfc6749.errors import MissingAuthorizationError

from .exceptions import ApiError, ValidationError


def register_error_handlers(app: Flask):
    """
    Registers error handlers for certain types of errors in a Flask application.

    """
    if app.config["DEBUG"]:
        app.logger.info("Disabling error handlers in development mode.")

    @app.errorhandler(MissingAuthorizationError)
    def handle_missing_authorization_error(err):
        return {
            "message": "User could not be authenticated, ensure correct headers are set."
        }, 401

    @app.errorhandler(ValidationError)
    def handle_validation_error(err):
        return err.to_dict()
