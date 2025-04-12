import array
import copy

a1 = array.array('I', range(5))
a2 = array.array('I', range(10, 15))
print(f'a1: {a1}')
print(f'a2: {a2}')
print(f'a1 + a2: {a1 + a2}')

a1 = array.array('I', range(5))
a2 = array.array('I', range(10, 15))
a1 += a2
print(f'a1: {a1}')
print(f'a2: {a2}')
print(f'a1 += a2: {a1}')

a1 = array.array('I', range(5))
print(f'a1: {a1}')
a1.append(99)
print(f'a1.append(99): {a1}')

a1 = array.array('I', range(5))
print(f'a1: {a1}')
print(f'2 in a1: {2 in a1}')

a1 = array.array('I', range(5))
a2 = copy.copy(a1)
print(f'a1 == a2: {a1 == a2}')
print(f'a1 is a2: {a1 is a2}')

a1 = array.array('I', range(5))
print(f'a1: {a1}')
print(f'a1.count(10): {a1.count(10)}')

a1 = array.array('I', range(5))
a2 = copy.deepcopy(a1)
print(f'a1 == a2: {a1 == a2}')
print(f'a1 is a2: {a1 is a2}')

a1 = array.array('I', range(5))
print(f'a1: {a1}')
del a1[0]
print(f'del a1[0]: {a1}')

a1 = array.array('I', range(5))
print(f'a1: {a1}')
a1.extend(range(15, 20))
print(f'a1.extend(range(15, 20)): {a1}')

a1 = array.array('I', range(5))
print(f'a1: {a1}')
a1.fromlist([1, 3, 5])
print(f'a1.fromlist([1, 3, 5]): {a1}')

a1 = array.array('I', range(5))
print(f'a1: {a1}')
print(f'a1[-1]: {a1[-1]}')

a1 = array.array('I', range(5))
print(f'a1: {a1}')
print(f'a1.index(3): {a1.index(3)}')

a1 = array.array('I', range(5))
print(f'a1: {a1}')
a1.insert(-1, 99)
print(f'a1.insert(-1, 99): {a1}')

a1 = array.array('I', range(5))
print(f'a1.itemsize: {a1.itemsize}')

a1 = array.array('I', range(5))
it = iter(a1)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

a1 = array.array('I', range(5))
print(f'len(a1): {len(a1)}')

a1 = array.array('I', range(5))
print(f'a1: {a1}')
print(f'a1 * 2: {a1 * 2}')

a1 = array.array('I', range(5))
print(f'a1: {a1}')
a1 *= 2
print(f'a1 *= 2: {a1}')

a1 = array.array('I', range(5))
print(f'a1: {a1}')
print(f'2 * a1: {2 * a1}')

a1 = array.array('I', range(5))
while a1:
    print(a1.pop())

a1 = array.array('I', range(5))
print(f'a1: {a1}')
a1.remove(3)
print(f'a1.remove(3): {a1}')

a1 = array.array('I', range(5))
print(f'a1: {a1}')
a1.reverse()
print(f'a1.reverse(): {a1}')

a1 = array.array('I', range(5))
print(f'a1: {a1}')
a1[-1] = 99
print(f'a1[-1] = 99: {a1}')

a1 = array.array('I', range(5))
print(f'a1: {a1}')
print(f'a1.tolist(): {a1.tolist()}')

a1 = array.array('I', range(5))
print(f'a1.typecode: {a1.typecode}')
