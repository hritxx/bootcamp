from .core import to_uppercase, to_snakecase
from processor_types import ProcessorFn

def get_pipeline(mode: str) -> list[ProcessorFn]:
    if mode == "uppercase":
        return [to_uppercase]
    elif mode == "snakecase":
        return [to_snakecase]
    else:
        raise ValueError(f"Unsupported mode: {mode}")