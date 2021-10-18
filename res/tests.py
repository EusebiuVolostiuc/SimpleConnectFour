import unittest
from ai import *
from human import *
from board import *
from engine import *

class TestBoard(unittest.TestCase):
    def setUp(self) -> None:
        self.__board = board()
        self.assertEqual(self.__board.rows,6)
        self.assertEqual(self.__board.columns,7)
        self.assertEqual(self.__board.get_val("X"), [])
        self.assertEqual(self.__board.get_val("O"), [])

    def testAdd(self):
        self.__board.put_val(1,"X")
        self.assertEqual(self.__board.get_val("X"),[51])
        self.__board.put_val(1,"O")
        self.assertEqual(self.__board.get_val("O"),[41])
        with self.assertRaises(ValueError):
            self.__board.put_val(0,"akjhk")
        self.assertEqual(self.__board.is_valid(1), 1)
        self.__board.put_val(1, "X")
        self.__board.put_val(1, "X")
        self.__board.put_val(1, "X")
        self.__board.put_val(1, "X")
        self.assertEqual(self.__board.put_val(1, "X"),-1)
        self.assertEqual(self.__board.is_valid(1), 0)

    def testReset(self):
        self.__board.put_val(1, "X")
        self.__board.put_val(1, "O")
        self.__board.reset()
        self.assertEqual(self.__board.get_val("X"), [])
        self.assertEqual(self.__board.get_val("O"), [])

    def testGets(self):
        self.__board.put_val(1, "X")
        self.__board.put_val(1, "O")
        self.__board.put_val(2, "X")
        self.assertEqual(self.__board.get_row(5),[" ","X","X"," "," "," "," "])
        self.assertEqual(self.__board.get_column(1), [" ", " ", " ", " ", "O", "X"])
        self.assertEqual(self.__board.get_matrix(),[[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                                    [' ', 'O', ' ', ' ', ' ', ' ', ' '],
                                                    [' ', 'X', 'X', ' ', ' ', ' ', ' ']])

class testEngine(unittest.TestCase):
    def setUp(self) -> None:
        self.__board = board()
        players = {"hX": Human("X"), "hO": Human("O")}
        self.__engine = engine(self.__board, players)

    def testA(self):
        self.__engine.set_players("hX","hO")
        self.__engine.move(1,1)
        self.__engine.move(2,1)
        self.__engine.move(1,2)
        self.assertEqual(self.__board.get_row(5), [" ", "X", "X", " ", " ", " ", " "])
        self.assertEqual(self.__board.get_column(1), [" ", " ", " ", " ", "O", "X"])
        self.assertEqual(self.__engine.is_won(),0)
        self.__engine.move(1, 3)
        self.__engine.move(1, 4)
        self.assertEqual(self.__engine.is_won(), "Player 1")

class testAI(unittest.TestCase):
    def setUp(self) -> None:
        self.__board = board()
        players = {"hX": Human("X")}
        self.__engine = engine(self.__board, players)
        players["AI"] = AI(self.__engine, 2)

    def testA(self):
        self.__engine.set_players("hX", "AI")
        self.__engine.move(2)
        assert "O" in self.__board.get_row(5)
        while self.__engine.is_won() == 0:
            self.__engine.move(2)
        self.assertEqual(self.__engine.is_won(), "Player 2")
