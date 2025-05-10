# LEGB Rule
x = 10
def f():
    x = 20
    print(x)
f()  # 20

# Nested Function Access
def outer():
    y = "outer var"
    def inner():
        print(y)
    inner()
outer()

# nonlocal
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        print(count)
    inner()
outer()

# global
x = 0
def update():
    global x
    x = 5
update()
print(x)  # 5

# Closure Function
def make_multiplier(n):
    def multiply(x):
        return n * x
    return multiply

triple = make_multiplier(3)
print(triple(10))  # 30

# Name Shadowing
len = 5
try:
    print(len("hello"))
except TypeError as e:
    print(e)  # 'int' object is not callable

# Scope Error
def oops():
    try:
        print(a)
        a = 1
    except UnboundLocalError as e:
        print(e)
oops()