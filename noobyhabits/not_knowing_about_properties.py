class JavaLike:
    def __init__(self, x):
        self._x = x

    def get_x(self):
        return self._x

    def set_x(self, x):
        # ...
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        self._x = val

def not_knowing_about_properties():
    obj = JavaLike(0)

    obj.set_x(42)
    print(obj.get_x())

    obj.x = 42
    print(obj.x)
