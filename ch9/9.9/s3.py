import time
import functools
import operator

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_lst = [repr(arg) for arg in args]
        arg_lst.extend(f'{k}={v!r}' for k, v in kwargs.items())
        arg_str = ', '.join(arg_lst)
        print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}')
        return result
    return clocked

def my_cache(func):
    hist = {}

    def dec_func(arg):
        if arg not in hist:
            hist[arg] = func(arg)
        return hist[arg]

    return dec_func

@my_cache
@clock
def fibonacci(n):
    return n if n < 2 else fibonacci(n - 2) + fibonacci(n - 1)

@clock
def fibonacci_new(n):
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

print(fibonacci(6))
