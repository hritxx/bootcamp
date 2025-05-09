from typing import Iterator, Dict, Any
from processors.base import ConfigurableStreamProcessor

class LineSplitter(ConfigurableStreamProcessor):

    def __init__(self, config: Dict[str, Any] = None):
        super().__init__(config)
        self.delimiter = self.config.get("delimiter", ",")
        self.max_splits = self.config.get("max_splits", -1)
    
    def process(self, lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            parts = line.split(self.delimiter, self.max_splits)
            for part in parts:
                yield part.strip()

def create_line_splitter(config: Dict[str, Any] = None) -> LineSplitter:

    return LineSplitter(config)
