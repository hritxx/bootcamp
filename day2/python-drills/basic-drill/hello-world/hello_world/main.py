import typer
import logging
from .hello import say_hello

app = typer.Typer()

@app.command()
def main(name: str, verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose logging")):

    if verbose:
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    else:
        logging.basicConfig(level=logging.WARNING)
        
    result = say_hello(name)
    typer.echo(result)

if __name__ == "__main__":
    app()
