from array import array
import math

class Vector2d:
    typecode = 'd'
    __match_args__ = ('x', 'y')

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        cls_name = type(self).__name__
        return '{}({!r}, {!r})'.format(cls_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        compnents = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*compnents)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __hash__(self):
        return hash((self.x, self.y))

    def __complex__(self):
        return complex(self.x, self.y)

def positional_pattern_demo(v: Vector2d) -> None:
    match v:
        case Vector2d(0, 0):
            print(f'{v!r} is null')
        case Vector2d(0):
            print(f'{v!r} is vertical')
        case Vector2d(_, 0):
            print(f'{v!r} is horizontal')
        case Vector2d(x, y) if x == y:
            print(f'{v!r} is diagonal')
        case _:
            print(f'{v!r} is awesome')

positional_pattern_demo(Vector2d(0, 0))
positional_pattern_demo(Vector2d(0, 1))
positional_pattern_demo(Vector2d(1, 0))
positional_pattern_demo(Vector2d(1, 1))
positional_pattern_demo(Vector2d(3, 4))
