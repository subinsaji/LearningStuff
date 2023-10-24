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
    people: List[Person]


joe = Person('Joe', 25, 1.85, 'joe@dataquest.io', (40.748441, -73.985664))
mary = Person('Mary', 43, 1.67, 'mary@dataquest.io', (-73.985664, 40.748441))
    

print(People([joe, mary]))