class Pixel:
    __slots__ = ('x', 'y')

    def __repr__(self):
        return f'({self.x}, {self.y})'

p = Pixel()
p.x = 1
p.y = 2
print(p)
p.color = 'red'
print(p.__dict__)
