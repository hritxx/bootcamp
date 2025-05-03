from typing import Optional

def say_hello(name: Optional[str] = None) -> str:
    return f"Hello, {name or 'World'}!"