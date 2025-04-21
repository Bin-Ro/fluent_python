a = [('A', 1), ('B', 2), ('C', 3)]
d = dict(a)
print(d)

a = [('A', -1), ('B', 2), ('C', 3)]
d = {k: v for k, v in a if v > 0}
print(d)

def dump(**kwargs):
    return kwargs
print(dump(**{'x': 1}, y=2, **{'z': 3}))

print({'a': 0, **{'x': 1}, 'y': 2, **{'z': 3, 'x': 4}})

d1 = dict(a=1, b=3)
d2 = dict(a=2, b=4, c=6)
print(d1 | d2)

d1 = dict(a=1, b=3)
d2 = dict(a=2, b=4, c=6)
d1 |= d2
print(d1)
