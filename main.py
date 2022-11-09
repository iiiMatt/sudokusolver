from random import choices
from solver import BacktrackingSolver, str_to_board
from time import perf_counter
import numpy as np


def _02112022():
    board_str = '000500300070032005030760009000407008000000030250000907720309500890200000005000006'
    board = str_to_board(board_str)

    solution = BacktrackingSolver(board).solve()
    print(solution)


def dummy_benchmark(n):
    test_cases = []
    with open('hard_sudokus_solved.txt', 'r') as f:
        lines = f.read().splitlines()[1:]

        for line in lines:
            board_str, solution_str = line.split(',')
            test_cases.append((str_to_board(board_str), str_to_board(solution_str)))

    start = perf_counter()
    for test_case in choices(test_cases, k=n):
        assert np.array_equal(BacktrackingSolver(test_case[0]).solve(), test_case[1])
    end = perf_counter()
    print(f'Time took to solve {n} sudokus: {end - start}')


def main():
    dummy_benchmark(50)


if __name__ == '__main__':
    main()
