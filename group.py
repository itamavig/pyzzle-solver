from dataclasses import dataclass
from typing import List

from IIdentifiable import IIdentifiable
from cell import Cell
from common import GlobalParameters


class Group(IIdentifiable):

    def __init__(self, group_cells: List[Cell], possibilities: List[int]):
        super().__init__()  # Creates Identifier for instance
        self.group_cells = group_cells
        GlobalParameters.all_groups[self.id] = self

    def _assign_value(self, cell_id, value):
        value_exists_in_group = value in self._get_assigned_values().values()
        cell_already_has_different_value = self._get_assigned_values().get(cell_id) != value
        cell_already_has_this_value = self._get_assigned_values().get(cell_id) == value
        if value_exists_in_group:
            cell_with_this_value_id = None
            for c in self.group_cells:
                if c.value == value:
                    cell_with_this_value_id = c.id
            raise Exception(f"Logical Flaw Error: Tried to assign value {value} in group {self.id},\n"
                            f"but this value already exists in cell {cell_with_this_value_id}")
        if cell_already_has_different_value:
            raise Exception(f"Logical Flaw Error: Tried to assign value {value} to cell {cell_id}\n"
                            f"that already has the value {GlobalParameters.all_cells[cell_id].value}")
        if cell_already_has_this_value:
            print(f"Logical Redundancy Warning: program has been trying to assign \n"
                  f"to cell {cell_id} value {value} at least twice")
            return
        GlobalParameters.all_cells[cell_id].value = value

    def _get_assigned_values(self):
        current_group_values = dict()
        for c in self.group_cells:
            if c.value != 0:
                current_group_values[c.id] = c.value
        return current_group_values

