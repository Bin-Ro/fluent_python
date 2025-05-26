import unicodedata

for a in (chr(c) for c in range(ord('A'), ord('Z') + 1)):
    print(f'{a}: {unicodedata.name(a)}')
