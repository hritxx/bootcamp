
data = {'name': 'Alice'}
try:
    print("EAFP:", data['age'])
except KeyError:
    print("EAFP: 'age' not found")


if 'age' in data:
    print("LBYL:", data['age'])
else:
    print("LBYL: 'age' not found")


try:
    with open('nonexistent.txt') as f:
        content = f.read()
except FileNotFoundError:
    print("File not found (EAFP)")


class User:
    def __init__(self, name):
        self.name = name

user = User("Bob")
print(getattr(user, "email", "Not available"))


import os
filename = 'nonexistent.txt'
if not os.path.exists(filename):
    print("File doesn't exist - risky in multi-threaded env")


class SafeUser:
    def __getattr__(self, attr):
        return f"{attr} not found"

u = SafeUser()
print(u.email)


val = "abc"
try:
    num = int(val)
except ValueError:
    print("EAFP: Conversion failed")


x = "hello"
if isinstance(x, int):
    print(x + 1)
else:
    print("Not an integer (LBYL)")
