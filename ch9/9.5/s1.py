from dis import dis
b = 6
def f3(a):
    global b
    print(a)
    print(b)
    b = 9

def f1(a):
    print(a)
    print(b)
    b = 9

print('*' * 40)
dis(f3)
print('*' * 40)
dis(f1)
print('*' * 40)
