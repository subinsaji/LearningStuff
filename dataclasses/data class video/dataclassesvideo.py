from dataclasses import dataclass
from dataclasses import make_dataclass

@dataclass
class Position:
    name: str
    lon: float
    lat: float
    
pos = Position('Shillong', 10.8, 59.9)


Position = make_dataclass('Position', ['name', 'lat', 'lon'])

print(Position("Harwell Campus", 2, 4))
