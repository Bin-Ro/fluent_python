import os

a, b = 1, 2
print(a, b)
a, b = b, a
print(a, b)

t = (20, 8)
print(divmod(*t))
q, r = divmod(*t)
print(q, r)

_, filename = os.path.split('/home/me')
print(filename)

a, b, *rest = range(5)
print(a, b, rest)

a, b, *rest = range(3)
print(a, b, rest)

a, b, *rest = range(2)
print(a, b, rest)

a, *body, c, d = range(5)
print(a, body, c, d)

*head, b, c, d = range(5)
print(head, b, c, d)

def fun(a, b, c, d, *rest):
    return a, b, c, d, rest

print(fun(*{1, 2}, 3, *range(4, 7)))

print((*range(4), 4))
print([*range(4), 4])
print({*range(4), 4, *(5, 6, 7)})
