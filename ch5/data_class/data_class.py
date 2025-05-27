from dataclasses import dataclass
import dataclasses

@dataclass
class Coordinate:
    lat: float=0
    lon: float=0

moscow = Coordinate(lat=3, lon=2)
print(moscow)
print(dataclasses.asdict(moscow))
print([f.name for f in dataclasses.fields(moscow)])
print([f.default for f in dataclasses.fields(moscow)])
print(moscow.__annotations__)
print(dataclasses.replace(moscow, lat=10, lon=20))
