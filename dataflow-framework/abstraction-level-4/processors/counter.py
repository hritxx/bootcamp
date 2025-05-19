from typing import Iterator, Dict, Any
from processors.base import ConfigurableStreamProcessor

class LineCounter(ConfigurableStreamProcessor):

    def __init__(self, config: Dict[str, Any] = None):
        super().__init__(config)
        self.start_num = self.config.get("start_num", 1)
        self.format = self.config.get("format", "[{count}] {line}")
        self.count = self.start_num
    
    def process(self, lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            yield self.format.format(count=self.count, line=line)
            self.count += 1
        
    def reset(self):

        self.count = self.start_num

def create_line_counter(config: Dict[str, Any] = None) -> LineCounter:

    return LineCounter(config)
