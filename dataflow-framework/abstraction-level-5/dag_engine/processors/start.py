def emit_lines(lines):
    for line in lines:
        yield ("trim", line)