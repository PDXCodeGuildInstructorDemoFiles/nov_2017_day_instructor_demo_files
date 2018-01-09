import unittest

from ttt.coords_board import CoordsTTTBoard
from ttt.dict_board import DictTTTBoard

from python.ttt.list_board import ListTTTBoard


class BaseBoardTest:
    def setUp(self):
        self.board = self.board_class()

    def test_str(self):
        """Test that the magic string method on a full board works."""
        self.board.place_token(1, 1, 'X')
        self.board.place_token(0, 0, 'O')
        self.board.place_token(1, 0, 'X')
        self.assertEqual(str(self.board), 'O| | \nX|X| \n | | \n')

    def test_calc_winner_none(self):
        """Test that calculating a winner returns None when no winner."""
        self.board.place_token(1, 1, 'X')
        self.board.place_token(0, 0, 'O')
        self.board.place_token(1, 0, 'X')
        self.board.place_token(0, 2, 'O')
        self.assertEqual(self.board.calc_winner(), None)

    def test_winner_won(self):
        """Test that calculating a winner returns the winner."""

        self.board.place_token(1, 1, 'X')
        self.board.place_token(0, 0, 'O')
        self.board.place_token(1, 0, 'X')
        self.board.place_token(0, 2, 'O')
        self.board.place_token(1, 2, 'X')
        self.assertEqual(self.board.calc_winner(), 'X')


class TestCoordsTTTBoard(BaseBoardTest, unittest.TestCase):
    """Tests CoordsTTTBoard using BaseBoardTest test methods."""
    board_class = CoordsTTTBoard


class TestDictTTTBoard(BaseBoardTest, unittest.TestCase):
    """Tests DictTTTBoard using BaseBoardTest test methods."""
    board_class = DictTTTBoard


class TestListListTTTBoard(BaseBoardTest, unittest.TestCase):
    """Tests ListListTTTBoard using BaseBoardTest test methods."""
    board_class = ListTTTBoard