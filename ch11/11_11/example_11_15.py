class Pixel:
    __slots__ = ('x', 'y')

    def __repr__(self):
        return f'({self.x}, {self.y})'

class ColorPixel(Pixel):
    __slots__ = ('color',)

cp = ColorPixel()
print(cp.__dict__)
cp.x = 2
cp.y = 3
cp.color = 'green'
cp.flavor = 'banana'
