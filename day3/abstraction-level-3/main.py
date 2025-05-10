from pathlib import Path
from typing import Optional
import typer
from dotenv import load_dotenv
import os

from pipeline import load_pipeline
from core import apply_pipeline

def process_command(
    input: Path = typer.Argument(...),
    output: Optional[Path] = typer.Option(None),
    config: Optional[Path] = typer.Option(Path("pipeline.yaml"))
):
    load_dotenv()
    processors = load_pipeline(config)
    with open(input, "r") as f:
        lines = f.readlines()

    processed_lines = [apply_pipeline(line.strip(), processors) for line in lines]

    if output:
        with open(output, "w") as f:
            f.write("\n".join(processed_lines))
    else:
        print("\n".join(processed_lines))