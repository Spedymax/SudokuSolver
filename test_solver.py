import unittest
import numpy as np
from solver import find_empty, valid, solve, get_board

class TestSudokuSolver(unittest.TestCase):
    def setUp(self):
        # Тестовая доска судоку
        self.test_board = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]

    def test_find_empty(self):
        # Тест поиска пустой ячейки
        empty_pos = find_empty(self.test_board)
        self.assertEqual(empty_pos, (0, 2))

    def test_valid(self):
        # Тест валидации числа в позиции
        # Тест для валидного числа
        self.assertTrue(valid(self.test_board, 3, (0, 2)))
        # Тест для невалидного числа (уже есть в строке)
        self.assertFalse(valid(self.test_board, 7, (0, 2)))
        # Тест для невалидного числа (уже есть в столбце)
        self.assertFalse(valid(self.test_board, 6, (0, 2)))

    def test_solve(self):
        # Тест решения судоку
        board_copy = [row[:] for row in self.test_board]
        self.assertTrue(solve(board_copy))
        # Проверяем, что все ячейки заполнены
        self.assertTrue(all(0 not in row for row in board_copy))

    def test_get_board(self):
        # Тест получения решенной доски
        solved_board = get_board(self.test_board)
        # Проверяем, что все ячейки заполнены
        self.assertTrue(all(0 not in row for row in solved_board))
        # Проверяем, что решение валидно
        for i in range(9):
            for j in range(9):
                self.assertTrue(valid(solved_board, solved_board[i][j], (i, j)))

if __name__ == '__main__':
    unittest.main() 