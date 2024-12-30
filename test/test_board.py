import pytest
from game_logic.board import Board
from exceptions.exceptions import InvalidArgumentException


def test_set_shape_valid():
    board = Board(5, 7)
    rows, columns = board.get_shape()
    assert rows == 5
    assert columns == 7


def test_set_shape_invalid():
    with pytest.raises(InvalidArgumentException):
        Board(-1, 5)
    with pytest.raises(InvalidArgumentException):
        Board(2, 0)