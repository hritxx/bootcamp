def trim(lines):
    for line in lines:
        yield ("tagger", line.strip())