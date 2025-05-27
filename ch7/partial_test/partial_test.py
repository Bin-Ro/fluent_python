import operator
import functools

print(list(map(functools.partial(operator.mul, 3), range(10))))
