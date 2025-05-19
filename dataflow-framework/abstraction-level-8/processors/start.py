from typing import Iterable, Tuple

def tag_lines(lines: Iterable[str]) -> Iterable[Tuple[str, str]]:
    for line in lines:
        line = line.strip()
        if line.lower().startswith("error"):
            yield ("error", line)
        elif line.lower().startswith("warn"):
            yield ("warn", line)
        else:
            yield ("general", line)