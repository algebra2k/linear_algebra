class Vec:
    def __init__(self, v):
        self._values = list.copy(v)

    def __iter__(self):
        """the vector iterator returned"""
        return self._values.__iter__()

    def __getitem__(self, index):
        return self._values.index(index)

    def __len__(self):
        return len(self._values)

    def __repr__(self):  
        return "Vector({})".format(self._values)

    def __str__(self):
        return "[{}]".format(", ".join(str(elem) for elem in self._values))

    def __add__(self, other):
        """向量加法, 返回结果向量"""
        assert len(self) == len(other), \
            "Error in adding, Length of vectors must be same"
        return Vec([a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __rmul__(self, other):
        pass

    def __pos__(self):
        pass

    def __neg__(self):
        pass

    def __radd__(self, other):
        pass
