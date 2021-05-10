from numbers import Number

class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def _get_x(self):
        return round(self._x)

    def _set_x(self, value):
        if not isinstance(value, Number):
            raise TypeError("...")
        self._x = value

    x = property(_get_x, _set_x)

    def _get_y(self):
        return round(self._x)

    def _set_y(self, value):
        if not isinstance(value, Number):
            raise TypeError("...")
        self._y = value

    y = property(_get_y, _set_y)