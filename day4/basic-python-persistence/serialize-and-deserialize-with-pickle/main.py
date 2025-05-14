import pickle

class Person:
    def __init__(self, name, institutions, colleagues):
        self.name = name
        self.institutions = institutions
        self.colleagues = colleagues


person = Person("Alice", ["MIT", "Stanford"], ["Bob", "Charlie"])
with open("person.pkl", "wb") as f:
    pickle.dump(person, f)


with open("person.pkl", "rb") as f:
    loaded_person = pickle.load(f)

print(loaded_person.__dict__)