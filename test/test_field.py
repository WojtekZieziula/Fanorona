import pytest
from game_logic.field import Field
from exceptions.exceptions import InvalidArgumentException


def test_set_value_valid():
    field_values = ["", "X", "O"]
    for value in field_values:
        Field(value)
    field = Field()


def test_set_value_invalid():
    with pytest.raises(InvalidArgumentException):
        Field("-")
