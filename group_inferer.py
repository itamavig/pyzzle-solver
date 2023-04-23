from typing import List

from common import GlobalParameters
from group import Group


def _infer_all_groups(board):
    groups: List[Group] = []
    groups.extend(list(_groups_from_rows(board)))
    groups.extend(list(_groups_from_columns(board)))
    groups.extend(list(_groups_from_boxes(board)))
    return groups


def _groups_from_rows(board):
    for row in board.grid:
        yield Group(group_cells=row, possibilities=GlobalParameters.possibilities)


def _groups_from_columns(board):
    for col in board.grid.T:
        yield Group(group_cells=col, possibilities=GlobalParameters.possibilities)


def _groups_from_boxes(board):
    for box_row in range(3):
        for box_col in range(3):
            cell_list = board.grid[
                        3 * box_row: 3 * (box_row + 1),
                        3 * box_col: 3 * (box_col + 1)
                        ]
            yield Group(group_cells=cell_list, possibilities=GlobalParameters.possibilities)


def infer_groups_from_grid(grid):
    return _infer_all_groups(grid)
