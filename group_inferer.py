from board import Board
from common import GlobalParameters
from group import Group


class _GroupInfer:
    def __init__(self, board: Board):
        self.board = board
        self._infer_all_groups()

    def _infer_all_groups(self):
        self._groups_from_rows()
        self._groups_from_columns()
        self._groups_from_boxes()

    def _groups_from_rows(self):
        for row in self.board.grid:
            Group(group_cells=row, possibilities=GlobalParameters.possibilities)

    def _groups_from_columns(self):
        for col in self.board.grid.T:
            Group(group_cells=col, possibilities=GlobalParameters.possibilities)

    def _groups_from_boxes(self):
        for box_row in range(3):
            for box_col in range(3):
                cell_list = self.board.grid[
                            3 * box_row: 3 * (box_row + 1),
                            3 * box_col: 3 * (box_col + 1)
                            ]
                Group(group_cells=cell_list, possibilities=GlobalParameters.possibilities)


def infer_groups_from_board(board: Board):
    _GroupInfer(board)
