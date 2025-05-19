def tag_lines(lines):
    for _, line in lines:
        line = line.strip()
        if "error" in line.lower():
            yield ("error", line)
        elif "warn" in line.lower():
            yield ("warn", line)
        else:
            yield ("general", line)