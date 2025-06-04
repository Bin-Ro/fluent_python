def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager

avg = make_averager()

print(avg(10))
print(avg(11))
print(avg(12))

print(f'avg.__code__.co_varnames: {avg.__code__.co_varnames}')
print(f'avg.__code__.co_freevars: {avg.__code__.co_freevars}')
print(f'avg.__closure__: {avg.__closure__}')
print(f'avg.__closure__[0].cell_contents: {avg.__closure__[0].cell_contents}')
