from solver import BacktrackingSolver, str_to_board


def _02112022():
    board_str = '000500300070032005030760009000407008000000030250000907720309500890200000005000006'
    board = str_to_board(board_str)

    solution = BacktrackingSolver.solve(board)
    print(solution)


def main():
    _02112022()


if __name__ == '__main__':
    main()
