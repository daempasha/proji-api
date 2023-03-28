"""A list of tests for ./app.py"""
import os
from flask import Flask
from . import get_config_path, mock_path_dict


class TestGetConfigPath:
    """A collection of tests related to get_config_path function."""

    def test_default(self, app: Flask):
        """Test the default output of the get_config_path function."""
        config = get_config_path(app)
        assert config == "api.config.Testing"

    @mock_path_dict(os.environ, TESTING="0")
    def test_development(self, app: Flask):
        """Test environment is switching to development properly."""
        app.config.update({"DEBUG": True})
        config = get_config_path(app)
        assert config == "api.config.Development"

    @mock_path_dict(os.environ, TESTING="0")
    def test_production(self, app: Flask):
        """Test environment is switching to production properly."""
        app.config.update({"DEBUG": False})

        config = get_config_path(app)
        assert config == "api.config.Production"
