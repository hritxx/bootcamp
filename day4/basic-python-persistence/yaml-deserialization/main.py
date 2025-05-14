import yaml

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car = Car("Toyota", "Camry")
yaml_str = yaml.dump(car.__dict__)
print(yaml_str)

yaml_input = """
brand: Toyota
model: Camry
"""

data = yaml.safe_load(yaml_input)
car = Car(**data)
print(car.__dict__)