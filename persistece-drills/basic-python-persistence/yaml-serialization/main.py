import yaml

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car = Car("Toyota", "Camry")
yaml_str = yaml.dump(car.__dict__)
print(yaml_str)