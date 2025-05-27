import operator
import collections

a = tuple(range(1, 10, 2))
print(a)

print(operator.itemgetter(1, 0)(a))

City = collections.namedtuple('City', 'name lat lon')

moscow = City(name='moscow', lat=2, lon=3)
print(moscow)
print(operator.attrgetter('lon', 'lat')(moscow))
