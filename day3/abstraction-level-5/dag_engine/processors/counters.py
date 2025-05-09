def count_errors(lines):
    for line in lines:
        print(f"ERROR COUNTED: {line}")
        yield ("end", line)

def count_warnings(lines):
    for line in lines:
        print(f"WARNING COUNTED: {line}")
        yield ("end", line)