from typing import Dict

from cell import Cell
from group import Group


class GlobalParameters:
    all_groups = Dict[int, Group]
    all_cells = Dict[int, Cell]
