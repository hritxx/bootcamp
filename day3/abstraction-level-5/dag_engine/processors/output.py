def terminal(lines):
    for line in lines:
        print(f"OUTPUT: {line}")
        yield ("end", line)