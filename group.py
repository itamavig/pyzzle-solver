from dataclasses import dataclass
from typing import List

from IIdentifiable import IIdentifiable
from cell import Cell

groups = dict()


class Group(IIdentifiable):

    def __init__(self, group_cells: List[Cell], possibilities: List[int]):
        super().__init__()
        self.value_mapping = dict()
        for cell in group_cells:
            self.value_mapping[cell.id] = 0
        groups[self.id] = self
        
    def _assign_value(self, cell_id, value):
        if value in self.value_mapping.values():
            raise Exception("Logical Flaw Error: Tried to assign a value in a group \n"
                            "in which the value already exists")
