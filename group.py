from dataclasses import dataclass
from typing import List
from cell import Cell


class Group:
    _recent_id = -1

    def __init__(self, cells: List[Cell], possibilities: List[int]):
        self.value_mapping = dict()
        for cell in cells:
            self.value_mapping[cell.id] = 0

    def _assign_value(self, cell_id, value):
        if value in self.value_mapping.values():
            raise Exception("Logical Flaw Error: Tried to assign a value in a group \n"
                            "in which the value already exists")



