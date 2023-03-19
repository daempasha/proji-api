from .main import two_plus_two


def test_two_plus_two(client):
    assert two_plus_two() == 4
