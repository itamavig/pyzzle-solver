from pprint import pprint

from cell import Cell


class Board:
    def __init__(self):
        self.grid = [[Cell() for i in range(9)] for j in range(9)]

    def display(self):
        pprint(self.grid)


if __name__ == '__main__':
    b = Board()
    pprint(b.grid)
    # b.grid[0][0] =
    pprint(b.grid)
