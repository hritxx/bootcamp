import contextlib
import tempfile
import time


try:
    with open('example.txt', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")


try:
    with open('file1.txt'), open('file2.txt'):
        pass
except FileNotFoundError:
    print("One of the files not found")


class Logger:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

with Logger():
    print("Inside the block")


@contextlib.contextmanager
def timer():
    start = time.time()
    yield
    print("Elapsed:", time.time() - start)

with timer():
    time.sleep(1)


with contextlib.suppress(FileNotFoundError):
    with open("missing.txt") as f:
        print(f.read())

with tempfile.TemporaryFile(mode='w+t') as f:
    f.write("Temporary data")
    f.seek(0)
    print(f.read())

class DBConnection:
    def __enter__(self):
        print("Opening DB")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing DB")

with DBConnection():
    print("Using DB")


class SafeOp:
    def __enter__(self):
        print("Start")
        return self
    def __exit__(self, exc_type, exc_value, tb):
        print("Cleanup")

try:
    with SafeOp():
        raise ValueError("Oops")
except ValueError:
    print("Handled error")
