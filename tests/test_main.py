import pytest
from my_awesome_project.main import add_numbers


def test_add_positive_numbers():
    assert add_numbers(2, 3) == 5


def test_add_negative_numbers():
    assert add_numbers(-1, -1) == -2


def test_add_mixed_numbers():
    assert add_numbers(-1, 1) == 0
