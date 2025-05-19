from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    age: int
    country: str = "India"
    tags: list[str] = field(default_factory=list)

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative.")

    def is_adult(self) -> bool:
        return self.age >= 18


u1 = User(name="Alice", age=25)
print(u1.is_adult()) 
print(u1)