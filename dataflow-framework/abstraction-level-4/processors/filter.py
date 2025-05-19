from typing import Iterator, Dict, Any
from processors.base import ConfigurableStreamProcessor

class LineFilter(ConfigurableStreamProcessor):

    def __init__(self, config: Dict[str, Any] = None):
        super().__init__(config)
        self.min_length = self.config.get("min_length", 0)
        self.contains = self.config.get("contains", None)
        self.starts_with = self.config.get("starts_with", None)
    
    def process(self, lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            if len(line) < self.min_length:
                continue
                
            if self.contains and self.contains not in line:
                continue
                
            if self.starts_with and not line.startswith(self.starts_with):
                continue
                
            yield line

def create_line_filter(config: Dict[str, Any] = None) -> LineFilter:

    return LineFilter(config)
