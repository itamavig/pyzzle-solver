import numpy as np

from IIdentifiable import IIdentifiable
from group_inferer import infer_groups_from_grid

class Board(IIdentifiable):
    def __init__(self, grid: np.array):
        super().__init__()
        self.grid = grid
        self.groups = infer_groups_from_grid(self.grid)
        if self.groups is None:
            print("oof")