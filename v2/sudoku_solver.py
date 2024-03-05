from board import Board


class Grouper:
    def __init__(self, board: Board):
        self.board = board

    def generate_group(self):
        for i in range(9):
            yield self.board.grid[i]
        for i in range(9):
            yield self.board.grid[:][i]
        for i in range(3):
            for j in range(3):
                yield self.board.grid[3 * i:3 * (i + 1)][3 * j:3 * (j + 1)]


def main():
    board = Board()
    board.display()
    # grouper = Grouper(board)


if __name__ == '__main__':
    main()
