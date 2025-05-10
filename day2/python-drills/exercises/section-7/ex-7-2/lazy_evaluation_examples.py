import sys
from itertools import islice


def read_large_file(filename):
    with open(filename) as f:
        for line in f:
            yield line


gen = (x*x for x in range(1000000))
lst = [x*x for x in range(1000000)]
print(f"Generator size: {sys.getsizeof(gen)} bytes")
print(f"List size: {sys.getsizeof(lst)} bytes")


def lazy_csv_filter(lines):
    for row in lines:
        if "ERROR" in row:
            yield row


print(any(x % 99 == 0 for x in range(1, 10_000_000)))


gen_lines = (f"line {i}" for i in range(100))
print(list(islice(gen_lines, 10)))


def yield_numbers(n):
    for i in range(n):
        yield i

for num in yield_numbers(5):
    print(num, end=" ")