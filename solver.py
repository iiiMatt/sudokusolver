from abc import ABC, abstractmethod
from copy import copy

SudokuBoard = list[int]


def str_to_board(board_str: str) -> SudokuBoard:
    return list(map(int, board_str))


def board_to_str(board: SudokuBoard) -> str:
    return ''.join(map(str, board))


class Solver(ABC):
    def __init__(self, board: SudokuBoard):
        self.board = copy(board)

    @abstractmethod
    def solve(self) -> SudokuBoard:
        pass


class BacktrackingSolver(Solver):
    def __init__(self, board: SudokuBoard):
        super().__init__(board)

        self.empty_cells = BacktrackingSolver._get_all_empty_cells(self.board)

        # contains which values are already in a row/col/box
        self.rows = [False] * 81
        self.cols = [False] * 81
        self.boxes = [False] * 81

        self._init_sections()

    def _init_sections(self):
        for row in range(9):
            for col in range(9):
                num = self.board[9 * row + col]
                if num > 0:
                    self._set_sections((row, col), num, True)

    def _set_sections(self, cell: (int, int), num: int, value: bool):
        row, col = cell
        self.rows[9 * row + num - 1] = value
        self.cols[9 * col + num - 1] = value
        self.boxes[9 * (3 * (row // 3) + (col // 3)) + num - 1] = value

    def solve(self) -> SudokuBoard:
        self._fill_board()
        return self.board

    def _fill_board(self):
        if not self.empty_cells:
            return True

        empty_cell = self.empty_cells.pop()

        row, col = empty_cell
        index = 9 * row + col

        for num in range(1, 10):
            if self.is_possible(empty_cell, num):
                self._set_sections(empty_cell, num, True)
                self.board[index] = num
                if self._fill_board():
                    return True
                self.board[index] = 0
                self._set_sections(empty_cell, num, False)

        self.empty_cells.append(empty_cell)

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
    def _get_all_empty_cells(board: SudokuBoard):
        empty_cells = []
        for row in range(9):
            for col in range(9):
                index = 9 * row + col
                if board[index] == 0:
                    empty_cells.append((row, col))

        return empty_cells

    def is_possible(self, cell: (int, int), num: int) -> bool:
        row, col = cell

        # Checking the row
        if self.rows[9 * row + num - 1]:
            return False

        # Checking the column
        if self.cols[9 * col + num - 1]:
            return False

        # Checking the box
        if self.boxes[9 * (3 * (row // 3) + (col // 3)) + num - 1]:
            return False

        return True
