from typing import Callable, Iterator, Dict, Any
from processor_types import ProcessorFn, StreamProcessor

class LineProcessorAdapter(StreamProcessor):
 
    def __init__(self, processor_fn: ProcessorFn):
        self.processor_fn = processor_fn
    
    def process(self, lines: Iterator[str]) -> Iterator[str]:
        for line in lines:
            yield self.processor_fn(line)

def adapt_processor(processor_fn: ProcessorFn) -> StreamProcessor:

    return LineProcessorAdapter(processor_fn)
