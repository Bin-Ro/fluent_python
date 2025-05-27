import operator
import functools

print(functools.reduce(operator.add, range(1, 101)))
print(sum(range(1, 101)))
