import typing

class Coordinate(typing.NamedTuple):
    lat: float = 0
    lon: float = 0

moscow = Coordinate(lat=2, lon=3)
print(moscow)
moscow_dict = moscow._asdict()
print(moscow_dict)
print(moscow._fields)
print(moscow._field_defaults)
print(moscow.__annotations__)
print(moscow._replace(lat=10, lon=20))
