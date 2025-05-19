from pathlib import Path
from typing import Optional, Iterator
import typer
from dotenv import load_dotenv
import os

from pipeline import load_pipeline
from core import apply_pipeline_stream

def read_lines(input_path: Path) -> Iterator[str]:

    with open(input_path, "r") as f:
        for line in f:
            yield line.rstrip('\n')

def process_command(
    input: Path = typer.Argument(..., help="Input file path"),
    output: Optional[Path] = typer.Option(None, help="Output file path"),
    config: Path = typer.Option(Path("pipeline.yaml"), help="Pipeline configuration file")
):
    load_dotenv()
    

    processors = load_pipeline(config)
    

    input_lines = read_lines(input)
    

    processed_lines = apply_pipeline_stream(input_lines, processors)
    

    if output:
        with open(output, "w") as f:
            for line in processed_lines:
                f.write(line + "\n")
    else:
        for line in processed_lines:
            print(line)
