from typing import Iterable, Tuple

def snakecase(lines: Iterable[str]) -> Iterable[Tuple[str, str]]:
    for line in lines:
        cleaned = line.strip().replace(" ", "_").lower()
        yield ("end", cleaned)