import pytest


@pytest.fixture(scope="session")
def number():
    return 10000


@pytest.fixture(scope="session")
def reroll_target():
    return 4


@pytest.fixture(scope="session")
def value():
    return [1, 1, 1, 1, 1, 1]
