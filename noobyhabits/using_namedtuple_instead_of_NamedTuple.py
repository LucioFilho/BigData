import collections
import typing

def using_namedtuple_instead_of_NamedTuple():
    Point = collections.namedtuple("Point", ["x", "y", "z"])
    p = Point(1, 2, 3)
    print(p.x + p.y + p.z)

    class Point(typing.NamedTuple):
        x: float
        y: float
        z: float

    p = Point(1, 2, 3)
    print(p.x + p.y + p.z)

