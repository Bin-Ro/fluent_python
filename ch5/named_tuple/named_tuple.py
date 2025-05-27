from collections import namedtuple
import json

Coordinate = namedtuple('Coordinate', 'lat lon', defaults=[0, 0])
moscow = Coordinate(55.756,37.617)
print(moscow)
moscow_dict = moscow._asdict()
print(moscow_dict)
json_moscow_dict = repr(json.dumps(moscow_dict))
print(json_moscow_dict)
print(moscow._fields)
print(moscow._field_defaults)
print(moscow._replace(lat=2, lon=3))
