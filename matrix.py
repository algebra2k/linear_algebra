class matrix:
    def __init__(self, list2d):
        self._values = [row[:] for row in list2d]

    def __repr__(self):
        return self._values

    def shape(self):
        pass