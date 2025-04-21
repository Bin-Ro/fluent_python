a = (1, 'alpha', [1, 2])
b = (1, 'alpha', [1, 2])

print(f'a: {a}')
print(f'b: {b}')
print(f'a == b: {a == b}')

b[-1].append(-99)
print(f'a: {a}')
print(f'b: {b}')
print(f'a == b: {a == b}')
