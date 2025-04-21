def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True

tf = (10, 'alpha', (1, 2))
tm = [10, 'alpha', (1, 2)]

print(f'fixed({tf}): {fixed(tf)}')
print(f'fixed({tm}): {fixed(tm)}')
