import unittest
from random import choices
from solver import BacktrackingSolver, str_to_board, board_to_str
import numpy as np


class SolverTest(unittest.TestCase):
    board_str = '000400970000051600042000010030000000070508064000070000700030000300090000005864009'
    board = np.array([
        0, 0, 0,  4, 0, 0,  9, 7, 0,
        0, 0, 0,  0, 5, 1,  6, 0, 0,
        0, 4, 2,  0, 0, 0,  0, 1, 0,

        0, 3, 0,  0, 0, 0,  0, 0, 0,
        0, 7, 0,  5, 0, 8,  0, 6, 4,
        0, 0, 0,  0, 7, 0,  0, 0, 0,

        7, 0, 0,  0, 3, 0,  0, 0, 0,
        3, 0, 0,  0, 9, 0,  0, 0, 0,
        0, 0, 5,  8, 6, 4,  0, 0, 9
    ])
    board2 = np.array([
        0, 2, 7, 8, 6, 5, 9, 1, 3,
        9, 0, 5, 2, 0, 3, 6, 8, 7,
        6, 8, 3, 7, 9, 1, 2, 0, 4,
        8, 7, 0, 6, 2, 9, 3, 4, 5,
        3, 4, 9, 1, 5, 8, 7, 2, 6,
        2, 5, 6, 3, 7, 4, 8, 9, 1,
        5, 9, 8, 4, 3, 7, 1, 6, 2,
        1, 3, 2, 5, 8, 6, 4, 7, 9,
        7, 6, 4, 9, 1, 2, 5, 3, 8,
    ])

    def test_backtracking_solver_init(self):
        solver = BacktrackingSolver(self.board2)

        # check empty cells
        self.assertEqual(solver.empty_cells, [(0, 0), (1, 1), (1, 4), (2, 7), (3, 2)])

    def test_str_to_board(self):
        board = str_to_board(self.board_str)
        self.assertTrue(np.array_equal(board, self.board))

    def test_board_to_str(self):
        board_str = board_to_str(self.board)
        self.assertTrue(np.array_equal(board_str, self.board_str))

    def test_is_possible(self):
        self.assertTrue(BacktrackingSolver(self.board).is_possible((2, 4), 8))  # possible
        self.assertFalse(BacktrackingSolver(self.board).is_possible((2, 4), 1))  # row
        self.assertFalse(BacktrackingSolver(self.board).is_possible((2, 4), 7))  # col
        self.assertFalse(BacktrackingSolver(self.board).is_possible((2, 4), 5))  # box

    def test_backtracking_solver1(self):
        board_str = '000400970000051600042000010030000000070508064000070000700030000300090000005864009'
        solutions_str = '513426978987351642642987513831649257279518364456273891798135426364792185125864739'

        board = str_to_board(board_str)
        solution = str_to_board(solutions_str)

        self.assertTrue(np.array_equal(BacktrackingSolver(board).solve(), solution))

    def test_backtracking_solver2(self):
        board_str = '000007490700165000000000000210000900907086013080000050800609700000500000030000020'
        solutions_str = '568327491794165382321948576216753948957486213483291657842619735179532864635874129'

        board = str_to_board(board_str)
        solution = str_to_board(solutions_str)

        self.assertTrue(np.array_equal(BacktrackingSolver(board).solve(), solution))

    def test_backtracking_solver_all(self):
        test_cases = []
        with open('hard_sudokus_solved.txt', 'r') as f:
            test_cases_str = f.read().splitlines()[1:]

            for test_case in test_cases_str:
                board_str, solution_str = test_case.split(',')

                test_cases.append(
                    (str_to_board(board_str), str_to_board(solution_str))
                )

        for _board, _solution in choices(test_cases, k=10):
            self.assertTrue(np.array_equal(BacktrackingSolver(_board).solve(), _solution))


if __name__ == '__main__':
    unittest.main()
