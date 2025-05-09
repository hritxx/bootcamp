from typing import Iterator, Dict, Any, List
from processors.base import ConfigurableStreamProcessor

class LineJoiner(ConfigurableStreamProcessor):

    def __init__(self, config: Dict[str, Any] = None):
        super().__init__(config)
        self.join_count = self.config.get("join_count", 2)
        self.separator = self.config.get("separator", " ")
        self.buffer: List[str] = []
    
    def process(self, lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            self.buffer.append(line)
            if len(self.buffer) >= self.join_count:
                yield self.separator.join(self.buffer)
                self.buffer = []
        

        if self.buffer:
            yield self.separator.join(self.buffer)
            self.buffer = []
    
    def reset(self):

        self.buffer = []

def create_line_joiner(config: Dict[str, Any] = None) -> LineJoiner:

    return LineJoiner(config)
