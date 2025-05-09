import typer
from dotenv import load_dotenv
import os

app = typer.Typer()


load_dotenv()
DEFAULT_MODE = os.getenv("MODE", "uppercase")

def read_lines(path: str):
    with open(path, "r") as f:
        for line in f:
            yield line.strip()

def transform_line(line: str, mode: str) -> str:
    if mode == "uppercase":
        return line.upper()
    elif mode == "snakecase":
        return line.strip().lower().replace(" ", "_")
    else:
        raise ValueError(f"Unsupported mode: {mode}")

def write_output(lines, output_path: str | None):
    if output_path:
        with open(output_path, "w") as f:
            for line in lines:
                f.write(line + "\n")
    else:
        for line in lines:
            print(line) 

@app.command()
def process(
    input: str = typer.Option(..., "--input", help="Input file path"),
    output: str = typer.Option(None, "--output", help="Output file path"),
    mode: str = typer.Option(DEFAULT_MODE, "--mode", help="Processing mode (uppercase/snakecase)"),
):
    lines = read_lines(input)
    transformed = (transform_line(line, mode) for line in lines)
    write_output(transformed, output)

if __name__ == "__main__":
    app()