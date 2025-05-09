from typing import Iterable, Tuple

def only_error(lines: Iterable[str]) -> Iterable[Tuple[str, str]]:
    for line in lines:
        yield ("general", f"ERROR DETECTED: {line}")

def only_warn(lines: Iterable[str]) -> Iterable[Tuple[str, str]]:
    for line in lines:
        yield ("end", f"WARNING COUNTED: {line}")