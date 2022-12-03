import numpy as np

from cell import Cell
from IIdentifiable import IIdentifiable


class Board(IIdentifiable):
    def __init__(self):
        super().__init__()
        self.grid = np.ndarray(shape=(9, 9), dtype=Cell)
