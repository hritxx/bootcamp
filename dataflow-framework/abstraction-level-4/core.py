from typing import Iterator, List
from processor_types import ProcessorFn, StreamProcessor

def apply_pipeline(line: str, processors: list[ProcessorFn]) -> str:
    for processor in processors:
        line = processor(line)
    return line

def apply_pipeline_stream(lines: Iterator[str], processors: List[StreamProcessor]) -> Iterator[str]:

    current_stream = lines
    for processor in processors:
        current_stream = processor(current_stream)
    return current_stream