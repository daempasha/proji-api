"""
This conftest.py file contains fixtures and configuration
options that are shared across multiple test files.
"""

import os
import pytest
from api import create_app


@pytest.fixture()
def app():
    """
    Fixture function that creates and configures a Flask application.

    Usage:
    - Use this fixture by including its name as a parameter in the test function.
    - The fixture function creates a Flask application and configures it.
    - The fixture function yields the application, so the test function can use it.k
    - Any code after the yield statement is executed after the test function completes.

    Returns:
    - The Flask application object that is provided by this fixture.

    """
    os.environ["TESTING"] = "1"
    application = create_app()
    yield application


@pytest.fixture()
def client(app):
    """
    Fixture function that provides a test client for a Flask application.

    Usage:
    - Use this fixture by including its name as a parameter in the test function.
    - The fixture function takes a Flask application as a dependency
    and creates a test client for it.
    - The fixture function returns the test client, so the test function can use it.

    Parameters:
    - app: The Flask application object to create a test client for.

    Returns:
    - A test client for the specified Flask application.

    """

    return app.test_client()


@pytest.fixture()
def runner(app):
    """
    Fixture function that creates a test runner for a Flask application.

    This fixture takes a Flask application as a parameter and returns a test runner for it.
    The `app.test_cli_runner()` method creates a test runner that
    can simulate command-line interface interactions with the application.
    The fixture provides the test runner object,
    which can be used in tests to test the behavior of your application's CLI commands.
    """

    return app.test_cli_runner()
