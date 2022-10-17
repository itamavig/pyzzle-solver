from abc import ABC


class IdGenerator:
    def __init__(self):
        self.counter = -1

    def __iter__(self):
        while True:
            self.counter += 1
            yield self.counter


class IIdentifiable(ABC):
    _counter = IdGenerator()

    def __init__(self):
        self._assign_id()

    def _create_id(self):
        for i in self._counter:
            yield i

    def _assign_id(self):
        self.id = self._create_id()
