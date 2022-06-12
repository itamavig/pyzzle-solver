"""
Class Cell.
This object represents a cell in a board puzzle.
"""


class Cell:
    """
    This object represents a cell in a board puzzle.
    """
    _recent_id = -1

    def __init__(self, possibilities_num):
        self.id = self._assign_id()
        self.possibilities = [i for i in range(1, possibilities_num + 1)]
        self.value = 0

    def __repr__(self):
        if self.value == 0:
            rep = f"Cell id = 0, \n" \
                  f"Cell possible values = {self.possibilities}"
        else:
            rep = f"Cell id = 0, \n" \
                  f"Cell value = {self.value}"
        return rep

    def _assign_id(self):
        Cell._recent_id += 1
        return self._recent_id

    def react_to_possibility_change(self):
        if len(self.possibilities) == 1:
            self.value = self.possibilities.pop()

    def remove_possibility(self, possibility):
        if possibility in self.possibilities:
            self.possibilities.remove(possibility)
            self.react_to_possibility_change()

