# Text Processor - Abstraction Level 4

## Overview

This is a text processing utility demonstrating abstraction level 4. The program introduces stream-based processing with stateful processors, allowing for powerful data transformations including fan-in, fan-out, and state management across lines.

## How It Works

The text processor now implements an advanced streaming architecture with:

1. **Stream Processing**: Processors work with iterators of strings rather than individual strings
2. **Stateful Processors**: Processors can maintain state between lines
3. **Fan-in/Fan-out Support**: Can merge multiple lines into one or split one line into many
4. **Backward Compatibility**: Adapters allow reuse of simple string processors
5. **Configurable Components**: Processors can be initialized with custom configuration
6. **Full Pipeline Integration**: All processors work together in a streaming pipeline

## Abstraction Level 4

This represents the fourth level of abstraction where:

- Processors operate on streams: `Iterator[str] -> Iterator[str]`
- The system can handle complex transformations that require maintaining state
- Processors can have different output counts than input counts
- Configuration parameters are passed directly to processors at initialization
- Adapters enable reuse of simpler processors
- The system supports both stateless and stateful processors

## Key Components

- **StreamProcessor Protocol**: Defines the interface for all stream processors
- **LineProcessorAdapter**: Adapts simple str->str processors to the stream interface
- **ConfigurableStreamProcessor**: Base class for processors that need configuration
- **Stateful Processors**: Processors that maintain state between processed lines
  - LineCounter: Adds line numbers to each line
  - LineJoiner: Combines multiple lines into one
  - LineSplitter: Splits one line into multiple lines
  - LineFilter: Filters lines based on criteria

## Usage

```bash
# Basic usage with default configuration
python cli.py input.txt

# Specify an output file
python cli.py input.txt --output out.txt

# Specify a custom pipeline configuration
python cli.py input.txt --config custom_pipeline.yaml
```

## Pipeline Configuration

The pipeline is configured in `pipeline.yaml`:

```yaml
pipeline:
  - type: processors.snake.to_snakecase
  - type: processors.splitter.create_line_splitter
    config:
      delimiter: ","
  - type: processors.counter.create_line_counter
    config:
      format: "{count}. {line}"
```

Each entry in the pipeline specifies:

- `type`: The fully qualified import path to the processor function or factory
- `config`: Optional configuration parameters for configurable processors

## Adding New Processors

### Simple String Processors

```python
# processors/reverse.py
def to_reverse(line: str) -> str:
    return line[::-1]
```

### Stream Processors

```python
# processors/custom_stream.py
from typing import Iterator, Dict, Any
from processors.base import ConfigurableStreamProcessor

class MyCustomProcessor(ConfigurableStreamProcessor):
    def __init__(self, config: Dict[str, Any] = None):
        super().__init__(config)
        self.my_param = self.config.get("my_param", "default")

    def process(self, lines: Iterator[str]) -> Iterator[str]:
        # Process the lines and yield results
        for line in lines:
            yield f"{self.my_param}: {line}"

def create_custom_processor(config: Dict[str, Any] = None) -> MyCustomProcessor:
    return MyCustomProcessor(config)
```

## Adding to Configuration

```yaml
pipeline:
  - type: processors.snake.to_snakecase
  - type: processors.custom_stream.create_custom_processor
    config:
      my_param: "Hello"
```

## Requirements

- Python 3.6+
- typer
- python-dotenv
- pyyaml
