from typing import Iterator
from processor_types import ProcessorFn

def to_uppercase(line: str) -> str:
    return line.upper()

def to_snakecase(line: str) -> str:
    return line.lower().replace(" ", "_")

def apply_processors(lines: Iterator[str], processors: list[ProcessorFn]) -> Iterator[str]:
    for line in lines:
        for processor in processors:
            line = processor(line)
        yield line