import typer
import logging
from typing import List
from hello_world import say_hello

app = typer.Typer()

@app.command()
def main(
    names: List[str], 
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose logging"),
    config_only: bool = typer.Option(False, "--config-only", "-c", help="Only log config loading messages")
):

    if verbose:

        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    elif config_only:

        logging.basicConfig(
            level=logging.WARNING,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        logging.getLogger('hello_world.config_loader').setLevel(logging.DEBUG)
    else:

        logging.basicConfig(level=logging.WARNING)
    
    for name in names:
        greeting = say_hello(name)
        typer.echo(greeting)

if __name__ == "__main__":
    app()
