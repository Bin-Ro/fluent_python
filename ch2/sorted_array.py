import array
a = array.array('I', [8, 4, 9, 2, 10])
print(a)
a = array.array(a.typecode, sorted(a))
print(a)
