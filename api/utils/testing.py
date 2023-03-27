"""Utils specifically for unit testing."""

from unittest import mock


def mock_path_dict(dict_to_override: dict, **envvars):
    """Decorator for mocking dict paths."""
    return mock.patch.dict(dict_to_override, envvars)
