import numpy as np

from cell import Cell
from IIdentifiable import IIdentifiable


class Board(IIdentifiable):
    def __init__(self, grid: np.array):
        super().__init__()
        self.grid = grid
