class Cell:
    def __init__(self):
        self.options = [i for i in range(1, 10)]
        self.value = 0

    def __repr__(self):
        return str(self.value)

    def assign_value_if_possible(self):
        if len(self.options) == 1:
            self.value = self.options[0]

    def remove_option(self, option):
        self.options.remove(option)
        self.assign_value_if_possible()


