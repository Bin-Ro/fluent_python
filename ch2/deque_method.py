from collections import deque
import copy

dq1 = deque(range(10), maxlen=10)
dq2 = deque(range(5), maxlen=5)
dq1 += dq2
print(dq1)

dq = deque(range(10), maxlen=10)
dq.append(99)
print(dq)

dq = deque(range(10), maxlen=10)
dq.appendleft(99)
print(dq)

dq = deque(range(10), maxlen=10)
dq.clear()
print(dq)

dq = deque(range(10), maxlen=10)
dq2 = copy.copy(dq)
print(dq == dq2)
print(dq is dq2)

dq = deque(range(10), maxlen=10)
print(dq.count(5))

dq = deque(range(10), maxlen=10)
del dq[5]
print(dq)

dq = deque(range(10), maxlen=10)
dq.extend(range(3))
print(dq)

dq = deque(range(10), maxlen=10)
dq.extendleft(range(3))
print(dq)

dq = deque(range(10), maxlen=10)
for i in range(len(dq)):
    print(dq[i])

dq = deque(range(10), maxlen=10)
it = iter(dq)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

dq = deque(range(10), maxlen=10)
while dq:
    print(dq.pop())
print(dq)

dq = deque(range(10), maxlen=10)
while dq:
    print(dq.popleft())
print(dq)

dq = deque(range(10), maxlen=10)
dq.remove(9)
print(dq)

dq = deque(range(10), maxlen=10)
dq.reverse()
print(dq)

dq = deque(range(10), maxlen=10)
for i in reversed(dq):
    print(i)

dq = deque(range(10), maxlen=10)
dq.rotate(3)
print(dq)

dq = deque(range(10), maxlen=10)
for i in range(len(dq)):
    dq[i] = 0
print(dq)
