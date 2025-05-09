from typing import Iterator, Dict, Any
from processor_types import StreamProcessor

class ConfigurableStreamProcessor(StreamProcessor):
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        
    def process(self, lines: Iterator[str]) -> Iterator[str]:
        raise NotImplementedError("Subclasses must implement process method")
    
    def __call__(self, lines: Iterator[str]) -> Iterator[str]:
        return self.process(lines)
