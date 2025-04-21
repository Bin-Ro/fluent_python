import array

symbols = 'Robin'
print(f'symbols: {symbols}')
print(f'tuple(ord(s) for s in symbols): {tuple(ord(s) for s in symbols)}')
print(f"array.array('I', (ord(s) for s in symbols)): {array.array('I', (ord(s) for s in symbols))}")

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

for cs in (f'{color} {size}' for color in colors for size in sizes):
    print(cs)
