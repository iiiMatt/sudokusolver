import unittest
from random import choices
from solver import BacktrackingSolver, str_to_board, board_to_str


class SolverTest(unittest.TestCase):
    board_str = '000400970000051600042000010030000000070508064000070000700030000300090000005864009'
    board = [
        0, 0, 0,  4, 0, 0,  9, 7, 0,
        0, 0, 0,  0, 5, 1,  6, 0, 0,
        0, 4, 2,  0, 0, 0,  0, 1, 0,

        0, 3, 0,  0, 0, 0,  0, 0, 0,
        0, 7, 0,  5, 0, 8,  0, 6, 4,
        0, 0, 0,  0, 7, 0,  0, 0, 0,

        7, 0, 0,  0, 3, 0,  0, 0, 0,
        3, 0, 0,  0, 9, 0,  0, 0, 0,
        0, 0, 5,  8, 6, 4,  0, 0, 9
    ]

    def test_str_to_board(self):
        board = str_to_board(self.board_str)
        self.assertEqual(board, self.board)

    def test_board_to_str(self):
        board_str = board_to_str(self.board)
        self.assertEqual(board_str, self.board_str)

    def test_is_possible(self):
        self.assertTrue(BacktrackingSolver.is_possible(self.board, (2, 4), 8))  # possible
        self.assertFalse(BacktrackingSolver.is_possible(self.board, (2, 4), 1))  # row
        self.assertFalse(BacktrackingSolver.is_possible(self.board, (2, 4), 7))  # col
        self.assertFalse(BacktrackingSolver.is_possible(self.board, (2, 4), 5))  # box

    def test_backtracking_solver1(self):
        board_str = '000400970000051600042000010030000000070508064000070000700030000300090000005864009'
        solutions_str = '513426978987351642642987513831649257279518364456273891798135426364792185125864739'

        board = str_to_board(board_str)
        solution = str_to_board(solutions_str)

        self.assertEqual(BacktrackingSolver.solve(board), solution)

    def test_backtracking_solver2(self):
        board_str = '000007490700165000000000000210000900907086013080000050800609700000500000030000020'
        solutions_str = '568327491794165382321948576216753948957486213483291657842619735179532864635874129'

        board = str_to_board(board_str)
        solution = str_to_board(solutions_str)

        self.assertEqual(BacktrackingSolver.solve(board), solution)

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
            self.assertEqual(BacktrackingSolver.solve(_board), _solution)


if __name__ == '__main__':
    unittest.main()
