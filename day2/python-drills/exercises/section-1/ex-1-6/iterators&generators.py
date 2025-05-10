# Manual Iterator
it = iter([1, 2, 3])
print(next(it))
print(next(it))

# Custom Iterator Class
class Counter:
    def __init__(self, max):
        self.max = max
        self.n = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.n < self.max:
            self.n += 1
            return self.n
        raise StopIteration

for val in Counter(3):
    print(val)

# Simple Generator
def countdown(n):
    while n > 0:
        yield n
        n -= 1
print(list(countdown(3)))

# Generator with State
def running_total(lst):
    total = 0
    for x in lst:
        total += x
        yield total
print(list(running_total([1, 2, 3])))

# Send to Generator
def echo():
    while True:
        received = yield
        print(f"Received: {received}")
e = echo()
next(e)  # Prime the generator
e.send("Hello")

# Generator Expression
print(list(x for x in range(10) if x % 2 == 0))

# Compare For Loop
def evens_gen():
    for x in range(10):
        if x % 2 == 0:
            yield x

print(list(evens_gen()))
print([x for x in range(10) if x % 2 == 0])