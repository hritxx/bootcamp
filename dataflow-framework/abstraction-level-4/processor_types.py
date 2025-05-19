from typing import Callable, Iterator, Protocol, TypeVar, Any, Dict


ProcessorFn = Callable[[str], str]


class StreamProcessor(Protocol):
    def process(self, lines: Iterator[str]) -> Iterator[str]:
        ...
    
    def __call__(self, lines: Iterator[str]) -> Iterator[str]:
        return self.process(lines)


ProcessorConfig = Dict[str, Any]


ProcessorFactory = Callable[[ProcessorConfig], StreamProcessor]
