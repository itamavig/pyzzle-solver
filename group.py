from dataclasses import dataclass
from typing import List

from IIdentifiable import IIdentifiable
from cell import Cell
from common import GlobalParameters


class Group(IIdentifiable):

    def __init__(self, group_cells: List[Cell], possibilities: List[int]):
        super().__init__()  # Creates Identifier for instance
        self.value_mapping = dict()
        for cell in group_cells:
            self.value_mapping[cell.id] = 0
        GlobalParameters.all_groups[self.id] = self

    def _assign_value(self, cell_id, value):
        value_exists_in_group = value in self.value_mapping.values()
        cell_already_has_different_value = self.value_mapping.get(cell_id) != value
        cell_already_has_this_value = self.value_mapping.get(cell_id) == value
        if value_exists_in_group:
            raise Exception("Logical Flaw Error: Tried to assign a value in a group \n"
                            "in which the value already exists")
        if cell_already_has_different_value:
            raise Exception("Logical Flaw Error: Tried to assign a value to a cell \n"
                            "that already has a different value")
        if cell_already_has_this_value:
            print(f"Logical Redundancy Warning: program has been trying to assign \n"
                  f"to cell {cell_id} value {value} at least twice")
            return
