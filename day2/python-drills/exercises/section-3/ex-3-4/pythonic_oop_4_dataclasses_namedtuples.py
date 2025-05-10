from dataclasses import dataclass, field
from typing import NamedTuple
from collections import namedtuple

@dataclass(frozen=True)
class User:
    name: str
    age: int = 0

    def is_adult(self):
        return self.age >= 18


@dataclass
class AdminUser(User):
    access_level: str = "admin"


u1 = User("Alice", 30)
u2 = User("Alice", 30)
print(u1 == u2)
print(u1.is_adult())

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)

BadPoint = namedtuple("BadPoint", ["x", "class"], rename=True)
print(BadPoint._fields)