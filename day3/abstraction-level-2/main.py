from .pipeline import get_pipeline
from .core import apply_processors
from processor_types import ProcessorFn

def read_lines(path: str):
    with open(path, 'r') as f:
        for line in f:
            yield line.strip()

def write_output(lines, output_path: str | None):
    if output_path:
        with open(output_path, 'w') as f:
            for line in lines:
                f.write(line + '\n')
    else:
        for line in lines:
            print(line)

def run(input_path: str, output_path: str | None, mode: str | None):
    import os
    mode = mode or os.getenv("MODE", "uppercase")
    pipeline = get_pipeline(mode)
    lines = read_lines(input_path)
    transformed = apply_processors(lines, pipeline)
    write_output(transformed, output_path)