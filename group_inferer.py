from typing import List

from board import Board
from common import GlobalParameters
from group import Group


class _GroupInfer:
    def __init__(self, board: Board):
        self._board = board
        self.groups = self._infer_all_groups()

    def _infer_all_groups(self):
        groups = List[Group]
        groups.extend(self._groups_from_rows())
        groups.extend(self._groups_from_columns())
        groups.extend(self._groups_from_boxes())
        return groups

    def _groups_from_rows(self):
        for row in self._board.grid:
            yield Group(group_cells=row, possibilities=GlobalParameters.possibilities)

    def _groups_from_columns(self):
        for col in self._board.grid.T:
            yield Group(group_cells=col, possibilities=GlobalParameters.possibilities)

    def _groups_from_boxes(self):
        for box_row in range(3):
            for box_col in range(3):
                cell_list = self._board.grid[
                            3 * box_row: 3 * (box_row + 1),
                            3 * box_col: 3 * (box_col + 1)
                            ]
                yield Group(group_cells=cell_list, possibilities=GlobalParameters.possibilities)

    def get_groups(self):
        return self.groups


def infer_groups_from_board(board: Board):
    return _GroupInfer(board).groups
