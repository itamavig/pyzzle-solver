from board import Board
from group import Group


class Grouper:
    def __init__(self, board: Board):
        self.board = board

    def get_groups(self):
        groups = []
        for row in range(9):
            groups.append(Group(self.board.grid[row, :]))
        for col in range(9):
            groups.append(Group(self.board.grid[:, col]))
        for row_block in range(3):
            for col_block in range(3):
                # print("hello")
                box = self.board.grid[3 * row_block:3 * (row_block + 1),
                                      3 * col_block:3 * (col_block + 1)]
                box = box.tolist()
                box_cells = []
                for l in box:
                    box_cells.extend(l)
                groups.append(Group(box_cells))
                # slice = [self.board.grid[3 * k:3 * (k + 1)][0:2] for k in range(0, 2)]
                # exit()
                # groups.append(Group(self.board.grid[3 * i:3 * (i + 1)][3 * j:3 * (j + 1)]))
        return groups


sudoku_board = [
    [1, 2, 5],
    [1, 3, 8],
    [1, 4, 4],
    [1, 6, 9],
    [1, 8, 2],
    [2, 5, 6],
    [2, 8, 8],
    [2, 9, 9],
    [3, 1, 2],
    [3, 3, 1],
    [3, 5, 3],
    [3, 7, 7],
    [4, 5, 1],
    [4, 6, 3],
    [4, 7, 4],
    [5, 1, 3],
    [5, 2, 2],
    [5, 5, 8],
    [5, 7, 9],
    [5, 9, 1],
    [6, 2, 7],
    [6, 3, 9],
    [6, 7, 6],
    [6, 9, 8],
    [7, 2, 6],
    [7, 6, 5],
    [7, 7, 8],
    [7, 8, 1],
    [7, 9, 7],
    [8, 1, 8],
    [8, 2, 1],
    [8, 3, 5],
    [8, 4, 7],
    [8, 7, 3],
    [8, 9, 4],
    [9, 2, 3],
    [9, 5, 9],
    [9, 7, 2]
]


def main():
    board = Board()
    # board.display()
    board.load(sudoku_board)
    board.display()
    grouper = Grouper(board)
    groups = grouper.get_groups()
    for i in range(10):
        for group in groups:
            group.check_for_values()
        board.display()


if __name__ == '__main__':
    main()
