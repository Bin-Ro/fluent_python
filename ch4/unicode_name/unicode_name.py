import unicodedata

al = [chr(c) for c in range(ord('A'), ord('Z') + 1)]
for a in al:
    print(f'{a}: {unicodedata.name(a)}')
