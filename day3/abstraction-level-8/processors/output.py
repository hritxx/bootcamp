from typing import Iterable, Tuple

def terminal(lines: Iterable[str]) -> Iterable[Tuple[str, str]]:
    for line in lines:
        print(f"[OUTPUT] {line}")
        yield ("end", line)