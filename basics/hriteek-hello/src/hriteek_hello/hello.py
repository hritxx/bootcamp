from typing import Optional
from rich import print

def say_hello(name: Optional[str] = None) -> None:
    print(f"[bold green]Hello, {name or 'World'}![/bold green]")
    
    
