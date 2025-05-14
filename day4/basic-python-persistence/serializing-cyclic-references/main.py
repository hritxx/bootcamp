import pickle

class A:
    def __init__(self):
        self.b = None

class B:
    def __init__(self):
        self.a = None

a = A()
b = B()
a.b = b
b.a = a

with open("cycle.pkl", "wb") as f:
    pickle.dump((a, b), f)

with open("cycle.pkl", "rb") as f:
    a_loaded, b_loaded = pickle.load(f)

print(a_loaded.b.a is a_loaded) 