import collections

def get_creators(record):
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f'Invalid record: {record!r}')

b1 = dict(api=1, author='Douglas Hofstadter', type='book', title='Godel, Escher, Bach')
print(get_creators(b1))
b2 = collections.OrderedDict(api=2, type='book', title='Python in a Nutshell', authors='Martelli Ravenscroft Holder'.split())
print(get_creators(b2))
