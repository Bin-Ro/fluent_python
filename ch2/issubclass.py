from collections import abc

print(f'issubclass(tuple, abs.Sequence): {issubclass(tuple, abc.Sequence)}')
print(f'issubclass(list, abc.Sequence): {issubclass(list, abc.MutableSequence)}')
