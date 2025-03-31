import random

s1 = [1, 2, 3]
s2 = [4, 5, 6]
print(f's1: {s1}')
print(f's2: {s2}')

print(f's1 + s2: {s1 + s2}')

s1 += [10, 12, 17]
print(f's1 += [10, 12, 17]: {s1}')

print(f's1: {s1}')
for i in range(100, 103):
    s1.append(i)
print(f's1: {s1}')

s1.clear()
print(f's1.clear(): {s1}')

print(f'2 in s1: {2 in s1}')

s1 = [1, 2, 3]
s2 = s1.copy()
print(f's1: {s1}')
print(f's2: {s2}')
print(f's1.count(2): {s1.count(2)}')

del s1[1]
print(f'del s[1]: {s1}')

print(f's1: {s1}')
s1.extend(range(15, 20))
print(f's1: {s1}')

print(f's1[0]: {s1[0]}')
print(f's1[-1]: {s1[-1]}')
print(f's1: {s1}')
print(f's1.index(16): {s1.index(16)}')

s1.insert(3, 10)
print(f's1.insert(3, 10): {s1}')

for e in s1:
    print(e)

print(f'len(s1): {len(s1)}')
print(f's1 * 2: {s1 * 2}')
print(f's1: {s1}')
s1 *= 2
print(f's1 *= 2: {s1}')
print(f'2 * s1: {2 * s1}')

while s1:
    print(s1.pop())

s1 = [1, 2, 3]
print(f's1: {s1}')
s1.remove(2)
print(f's1.remove(2): {s1}')
s1.reverse()
print(f's1.reverse(): {s1}')

print(f'list(reversed(list(range(10)))): {list(reversed(list(range(10))))}')

s1 = list(range(10))
random.shuffle(s1)
print(f's1: {s1}')
s1.sort()
print(f's1: {s1}')
