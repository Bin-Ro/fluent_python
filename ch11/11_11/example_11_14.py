class Pixel:
    __slots__ = ('x', 'y')

    def __repr__(self):
        return f'({self.x}, {self.y})'

class OpenPixel(Pixel):
    pass

op = OpenPixel()
print(op.__dict__)
op.x = 8
print(op.x)
print(op.__dict__)
op.color = 'green'
print(op.__dict__)
