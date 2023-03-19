"""Tests for main.py"""

from .main import two_plus_two


def test_two_plus_two(client):
    """Example test: 2+2=4"""
    assert two_plus_two() == 4
