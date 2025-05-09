def tag_lines(lines):
    for line in lines:
        if "error" in line.lower():
            yield ("error", line)
        elif "warn" in line.lower():
            yield ("warn", line)
        else:
            yield ("general", line)