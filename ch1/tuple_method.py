s = (1, 2, 3)
s2 = (7, 8, 9)
print(f's: {s}')
print(f's2: {s2}')
print(f's + s2: {s + s2}')

s = (1, 2, 3)
print(f's: {s}')
print(f'2 in s: {2 in s}')
print(f'0 in s: {0 in s}')

s = (1, 2, 3, 2, 3)
print(f's: {s}')
print(f's.count(0): {s.count(0)}')
print(f's.count(2): {s.count(2)}')
print(f's.count(1): {s.count(1)}')

s = (3, 9, 0)
for i in range(len(s)):
    print(s[i])

s = (1, 2, 3)
print(f's.index(1): {s.index(1)}')
print(f's.index(2): {s.index(2)}')
print(f's.index(0): {s.index(0)}')

s = (1, 2, 3)
it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

s = (1, 2, 3)
print(f's: {s}')
print(f'len(s): {len(s)}')

s = (1, 2, 3)
print(f's: {s}')
print(f's * 2: {s * 2}')

s = (1, 2, 3)
print(f's: {s}')
s *= 2
print(f's *= 2: {s}')

s = (1, 2, 3)
print(f's: {s}')
print(f'2 * s: {2 * s}')
