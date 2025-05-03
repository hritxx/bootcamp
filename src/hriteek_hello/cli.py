import typer
from hriteek_hello.hello import say_hello

app = typer.Typer()

@app.command()
def greet(name: str = typer.Option(None, help="Name to greet")):
    say_hello(name)

if __name__ == "__main__":
    app()