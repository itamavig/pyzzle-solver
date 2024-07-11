from typing import List
from pprint import pprint
import numpy as np
from cell import Cell


class Board:
    def __init__(self):
        self.grid = np.zeros(shape=(9, 9), dtype=Cell)
        self.configure()
        # self.grid = [[Cell() for i in range(9)] for j in range(9)]

    def configure(self):
        for row in range(9):
            for col in range(9):
                self.grid[row, col] = Cell()

    def display(self):
        pprint(self.grid)

    def load(self, specs: List[List]):
        for row, col, val in specs:
            self.grid[row - 1, col - 1].manual_set(val)


example_board = [
    [1, 2, 5],
    [1, 3, 8],
    [1, 4, 4],
    [1, 6, 9],
    [1, 8, 2],
    [2, 5, 6],
    [2, 8, 8],
    [2, 9, 9],
    [3, 1, 2],
    [3, 3, 1],
    [3, 5, 3],
    [3, 7, 7],
    [4, 5, 1],
    [4, 6, 3],
    [4, 7, 4],
    [5, 1, 3],
    [5, 2, 2],
    [5, 5, 8],
    [5, 7, 9],
    [5, 9, 1],
    [6, 2, 7],
    [6, 3, 9],
    [6, 7, 6],
    [6, 9, 8],
    [7, 2, 6],
    [7, 6, 5],
    [7, 7, 8],
    [7, 8, 1],
    [7, 9, 7],
    [8, 1, 8],
    [8, 2, 1],
    [8, 3, 5],
    [8, 4, 7],
    [8, 7, 3],
    [8, 9, 4],
    [9, 2, 3],
    [9, 5, 9],
    [9, 7, 2]
]

if __name__ == '__main__':
    b = Board()
    # b.display()
    b.load(example_board)
    # b.grid[0][0] =
    b.display()
    pprint(b.grid[0, :])
