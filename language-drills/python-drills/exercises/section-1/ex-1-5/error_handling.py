# try/except
try:
    1 / 0
except ZeroDivisionError:
    print("Cannot divide")

# try/except/else
try:
    print(10 / 2)
except ZeroDivisionError:
    print("Cannot divide")
else:
    print("Success")

# finally Block
try:
    x = 1 / 1
finally:
    print("Cleanup done")

# Multiple Exceptions
try:
    int("abc")
except ValueError:
    print("Value error!")
except ZeroDivisionError:
    print("Divide by zero!")

# Custom Exception
class InvalidAgeError(Exception): pass
age = -1
if age < 0:
    raise InvalidAgeError("Age can't be negative")

# Reraise Exception
try:
    raise ValueError("Something bad")
except ValueError as e:
    print("Logging:", e)
    raise

# Suppressing Exceptions
from contextlib import suppress
d = {"x": 1}
with suppress(KeyError):
    print(d["y"])

# Nested try Blocks
try:
    try:
        1 / 0
    except ZeroDivisionError:
        print("Inner caught")
        raise
except Exception:
    print("Outer caught")