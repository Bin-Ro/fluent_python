import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __iter__(self):
        return iter((self.x, self.y))

    def __reversed__(self):
        return reversed([self.x, self.y])

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __pos__(self):
        return Vector(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __imul__(self, scalar):
        self.x *= scalar
        self.y *= scalar
        return self

    def __rmul__(self, scalar):
        return self * scalar

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar)

    def __itruediv__(self, scalar):
        self.x /= scalar
        self.y /= scalar
        return self

    def __floordiv__(self, scalar):
        return Vector(self.x // scalar, self.y // scalar)

    def __ifloordiv__(self, scalar):
        self.x //= scalar
        self.y //= scalar
        return self

v1 = Vector(1, 2)
print(f'v1: {v1}')
print(f'abs(v1): {abs(v1)}')

print(f'bool(v1): {bool(v1)}')
print(f'bool(Vector()): {bool(Vector())}')

for i in v1:
    print(i)

for i in reversed(v1):
    print(i)

print(f'-v1: {-v1}')
print(f'+v1: {+v1}')

print(f'v1 == Vector(3, 4): {v1 == Vector(3, 4)}')
print(f'v1 != Vector(3, 4): {v1 != Vector(3, 4)}')

print(f'v1 + Vector(3, 4): {v1 + Vector(3, 4)}')
print(f'v1 - Vector(3, 4): {v1 - Vector(3, 4)}')
print(f'v1 * 2: {v1 * 2}')
print(f'2 * v1: {2 * v1}')
print(f'v1 / 2: {v1 / 2}')
print(f'v1 // 2: {v1 // 2}')

v1 += Vector(3, 4)
print(f'v1 += Vector(3, 4): {v1}')
v1 -= Vector(3, 4)
print(f'v1 -= Vector(3, 4): {v1}')
v1 *= 2
print(f'v1 *= 2: {v1}')
v1 /= 2
print(f'v1 /= 2: {v1}')
v1 //= 2
print(f'v1 //= 2: {v1}')
