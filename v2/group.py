from typing import List
from cell import Cell


class Group:
    def __init__(self, cells: List[Cell]):
        self.cells = cells
        self.options = [i for i in range(1, 10)]

    def remove_option(self, option):
        if option in self.options:
            self.options.remove(option)
            for cell in self.cells:
                if cell.value == 0:
                    cell.remove_option(option)

    def check_for_values(self):
        # print(self.cells)
        for cell in self.cells:
            # print(cell)
            if cell.value != 0:
                self.remove_option(cell.value)

    def display(self):
        print(f"cells: {[cell for cell in self.cells]}")
        print(f"remaining options: {self.options}")
