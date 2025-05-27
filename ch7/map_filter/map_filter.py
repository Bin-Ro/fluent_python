import operator
import functools

def fatorials(n):
    return functools.reduce(operator.mul, range(1, n + 1))

print(list(map(fatorials, range(1, 11))))
print([fatorials(n) for n in range(1, 11)])

print(list(map(fatorials, filter(lambda n: n % 2, range(1, 11)))))
print([fatorials(n) for n in range(1, 11) if n % 2])
