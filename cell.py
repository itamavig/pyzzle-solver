"""
Class Cell.
This object represents a cell in a board puzzle.
"""
from IIdentifiable import IIdentifiable
from common import GlobalParameters


class Cell(IIdentifiable):
    """
    This object represents a cell in a board puzzle.
    """
    _recent_id = -1

    def __init__(self, possibilities_num=9):
        super().__init__()  # Creates Identifier for instance
        self.possibilities = [i for i in range(1, possibilities_num + 1)]
        self.value = 0
        GlobalParameters.all_cells[self.id] = self

    def __str__(self):
        if self.value == 0:
            _str = f"Cell id = {self.id}, \n" \
                   f"Cell possible values = {self.possibilities}"
        else:
            _str = f"Cell id = {self.id}, \n" \
                   f"Cell value = {self.value}"
        return _str

    # def _assign_id(self):
    #     Cell._recent_id += 1
    #     return self._recent_id

    def _react_to_possibility_change(self):
        if len(self.possibilities) == 1:
            self.value = self.possibilities[0]

    def remove_possibility(self, possibility):
        if possibility in self.possibilities:
            self.possibilities.remove(possibility)
            self._react_to_possibility_change()
