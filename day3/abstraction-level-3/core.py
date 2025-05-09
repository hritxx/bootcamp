from processor_types import ProcessorFn

def apply_pipeline(line: str, processors: list[ProcessorFn]) -> str:
    for processor in processors:
        line = processor(line)
    return line