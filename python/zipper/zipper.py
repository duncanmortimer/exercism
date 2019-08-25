from functools import reduce


LEFT, VALUE, RIGHT = "left", "value", "right"


class Zipper:
    """
    A Binary-tree-with-zipper for python.
    """

    @property
    def _left_branch(self):
        return self._location[LEFT]

    @property
    def _right_branch(self):
        return self._location[RIGHT]

    @property
    def _value(self):
        return self._location[VALUE]

    @staticmethod
    def from_tree(tree):
        return Zipper(path=[], location=tree)

    def __init__(self, path, location):
        self._path = path
        self._location = location

    def value(self):
        return self._value

    def set_value(self, new_value):
        return Zipper(
            path=self._path,
            location={LEFT: self._left_branch, VALUE: new_value, RIGHT: self._right_branch}
        )

    def left(self):
        if self._left_branch is None:
            return None

        return Zipper(
            path=[lambda x: {LEFT: x, VALUE: self._value, RIGHT: self._right_branch}] + self._path,
            location=self._left_branch
        )

    def set_left(self, new_left):
        return Zipper(
            path=self._path,
            location={LEFT: new_left, VALUE: self._value, RIGHT: self._right_branch}
        )

    def right(self):
        if self._right_branch is None:
            return None

        return Zipper(
            path=[lambda x: {LEFT: self._left_branch, VALUE: self._value, RIGHT: x}] + self._path,
            location=self._right_branch
        )

    def set_right(self, new_right):
        return Zipper(
            path=self._path,
            location={LEFT: self._left_branch, VALUE: self._value, RIGHT: new_right}
        )

    def up(self):
        if not self._path[0]:
            return None

        return Zipper(
            path=self._path[1:],
            location=self._path[0](self._location)
        )

    def to_tree(self):
        return reduce(lambda v, f: f(v), self._path, self._location)
