from dataclasses import dataclass
from typing import Tuple
from typing import List


@dataclass
class Person():
    name: str
    age: int
    height: float
    email: str
    house_coords: Tuple


print(Person("Subin", 24, 1.77, "subin@subin.io", (51.5744, 1.3109)))