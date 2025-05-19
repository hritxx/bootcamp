def only_error(lines):
    for _, line in lines:
        yield ("general", f"ERROR DETECTED: {line}")

def only_warn(lines):
    for _, line in lines:
        yield ("end", f"WARNING COUNTED: {line}")