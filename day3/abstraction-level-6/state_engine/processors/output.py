def terminal(lines):
    for _, line in lines:
        print("OUTPUT:", line)
        yield ("end", line)