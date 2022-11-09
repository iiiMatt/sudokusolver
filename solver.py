from abc import ABC, abstractmethod
from copy import copy

SudokuBoard = list[int]


def str_to_board(board_str: str) -> SudokuBoard:
    return list(map(int, board_str))


def board_to_str(board: SudokuBoard) -> str:
    return ''.join(map(str, board))


class Solver(ABC):
    @staticmethod
    @abstractmethod
    def solve(board: SudokuBoard) -> SudokuBoard:
        pass


class BacktrackingSolver(Solver):
    @staticmethod
    def solve(board: SudokuBoard) -> SudokuBoard:
        res = copy(board)
        BacktrackingSolver._fill_board(res)
        return res

    @staticmethod
    def _fill_board(board: SudokuBoard):
        empty_cell = BacktrackingSolver._find_first_empty_cell(board)

        if empty_cell is None:
            return True
        row, col = empty_cell
        index = 9 * row + col

        for num in range(1, 10):
            if BacktrackingSolver.is_possible(board, empty_cell, num):
                board[index] = num
                if BacktrackingSolver._fill_board(board):
                    return True
                board[index] = 0

        return False

    @staticmethod
    def _find_first_empty_cell(board: SudokuBoard):
        for row in range(9):
            for col in range(9):
                index = 9 * row + col
                if board[index] == 0:
                    return row, col
        return None

    @staticmethod
    def is_possible(board: SudokuBoard, cell: (int, int), num: int) -> bool:
        row, col = cell

        # Checking the row
        for _col in range(9):
            if board[9 * row + _col] == num:
                return False

        # Checking the column
        for _row in range(9):
            if board[9 * _row + col] == num:
                return False

        # Checking the box
        box_id = 3 * (row // 3) + (col // 3)
        for i in range(3):
            for j in range(3):
                _row = 3 * (box_id // 3) + i
                _col = 3 * (box_id % 3) + j

                if board[9 * _row + _col] == num:
                    return False

        return True
