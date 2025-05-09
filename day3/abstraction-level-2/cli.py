import typer
from dotenv import load_dotenv
import os
from typing import Optional

app = typer.Typer()
load_dotenv()

@app.command()
def process(
    input: str,
    output: Optional[str] = None,
    mode: Optional[str] = typer.Option(None),
):
    from .main import run
    run(input, output, mode)