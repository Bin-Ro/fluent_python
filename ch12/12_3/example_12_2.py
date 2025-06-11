from array import array
import reprlib
import math

class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return f'Vector({components})'

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(self._components)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(*self)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

v1 = Vector([3.1, 4.2])
v2 = Vector((3, 4, 5))
v3 = Vector(range(10))
print(v1, v2, v3)
print(repr(v1), repr(v2), repr(v3))

for i in v3:
    print(i)
v1_bytes = bytes(v1)
print(v1_bytes)
print(len(v1_bytes))
print(repr(Vector.frombytes(v1_bytes)))
v2_bytes = bytes(v2)
print(v2_bytes)
print(len(v2_bytes))
print(repr(Vector.frombytes(v2_bytes)))
v3_bytes = bytes(v3)
print(v3_bytes)
print(len(v3_bytes))
print(repr(Vector.frombytes(v3_bytes)))
print(v1 == Vector([3.1, 4.2]))
print(abs(v1))
print(bool(Vector([0,])))
