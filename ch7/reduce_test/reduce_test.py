import operator
import functools

def factorial(n):
    return functools.reduce(operator.mul, range(1, n + 1))

print(factorial(10))
