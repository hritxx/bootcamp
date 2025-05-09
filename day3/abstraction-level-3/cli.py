# cli.py
import typer
from main import process_command

app = typer.Typer()
app.command()(process_command)

if __name__ == "__main__":
    app()