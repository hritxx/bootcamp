# Default Arguments
def greet(name="Guest"):
    print(f"Hello, {name}!")
greet()
greet("Sam")

# Keyword Arguments
def info(name, age=0):
    print(f"{name} is {age} years old.")
info(age=25, name="Tina")

# Variable Positional Args
def add_all(*args):
    return sum(args)
print(add_all(1, 2, 3))  # 6

# Variable Keyword Args
def show_settings(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} = {v}")
show_settings(theme="dark", font="Arial")

# Mixed Args
def example(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)
example(1, 2, a=3, b=4)

# Positional-Only Args
def f(x, /):
    print(x)
f(10)

# Keyword-Only Args
def f(*, x):
    print(x)
f(x=10)

# Function Annotations
def add(a: int, b: int) -> int:
    return a + b
print(add(2, 3))