import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        def clocked(*_args):
            t0 = time.perf_counter()
            _result = func(*_args)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result
        return clocked
    return decorate

@clock()
def snooze(seconds):
    time.sleep(seconds)

print('*' * 40)
for _ in range(3):
    snooze(.123)

@clock('{name}: {elapsed}s')
def snooze(seconds):
    time.sleep(seconds)

print('*' * 40)
for _ in range(3):
    snooze(.123)

@clock('{name}({args}) dt={elapsed:.3f}s')
def snooze(seconds):
    time.sleep(seconds)

print('*' * 40)
for _ in range(3):
    snooze(.123)
