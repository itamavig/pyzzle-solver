from typing import List
from cell import Cell


class Group:
    def __init__(self, cells: List[Cell]):
        self.cells = cells
        self.options = [i for i in range(1, 10)]

    def remove_option(self, option):
        self.options.remove(option)
        for cell in self.cells:
            cell.remove_option(option)

    def check_for_values(self):
        for cell in self.cells:
            if cell.value != 0:
                self.remove_option(cell.value)
