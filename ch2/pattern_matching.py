def fun(message):
    match message:
        case ['A', a, b, c]:
            print(f'["A", {a}, {b}, {c}]')
        case ['B', a, b]:
            print(f'["B", {a}, {b}]')
        case _:
            print('Unknown case')

message = ['A', 1, 2, 3]
fun(message)
message = ['B', 1, 2]
fun(message)
message = ['C']
fun(message)

records = [
        ('a', 2, 3, (4, 5)),
        ('b', 2, 3, (4, -5)),
        ('b', 2, 3, (4., -5.)),
        ('c', 2, 3, (4, 10)),
        ]

for record in records:
    match record:
        case [str(a), _, _, (float(b), float(c)) as t] if c < 0:
            print(f'{a}, {t}')

def fun2(phone):
    match tuple(phone):
        case ['1', *_]:
            print('1')
        case ['2', *_]:
            print('2')
        case ['3' | '4', *_]:
            print('3 | 4')
        case _:
            print('Unknown case')

phone = '135'
fun2(phone)

phone = '235'
fun2(phone)

phone = '335'
fun2(phone)

phone = '435'
fun2(phone)

phone = '535'
fun2(phone)
