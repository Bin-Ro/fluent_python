symbols = 'Robin'
print(f'symbols: {symbols}')
print(f'[ord(s) for s in symbols]: {[ord(s) for s in symbols]}')

l1 = [ord(s) for s in symbols if ord(s) % 2 == 0]
print(f'l1: {l1}')

l2 = list(filter(lambda s : s % 2 == 0, map(ord, symbols)))
print(f'l2: {l2}')
