from python3_poetry import __version__, multiply


def test_version() -> None:
    assert __version__ == '0.1.0'

def test_square() -> None:
    assert multiply(4, 3) == 9