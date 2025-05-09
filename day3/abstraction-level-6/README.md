# State Engine Log Processor

A flexible, tag-based state engine for processing log lines through a configurable pipeline.

## Architecture Overview

This project implements a state engine that processes input lines through a series of processor functions. Each processor is associated with a tag, and the output from each processor determines the next processor to be used based on the tag it emits.

```
[Input] → [start processor] → [error/warn/general processors] → [end processor] → [Output]
```

## Components

### Core Components

- **StateEngine**: The main engine that orchestrates the flow of data through processors
- **Processors**: Functions that take lines with tags and yield new tagged lines
  - **start.py**: Initial tagging of input lines based on content
  - **filters.py**: Specialized processors for error and warning lines
  - **formatters.py**: Text transformation processors
  - **output.py**: Final output processors

### Data Flow

1. Input lines enter the system
2. Each line is tagged with "start" and added to the queue
3. Processors consume and produce tagged lines
4. Lines move through the system until they reach an "end" tag

## Usage

1. Create a configuration file (YAML) defining the nodes and processors
2. Instantiate the StateEngine with the config file path
3. Run the engine with your input data

```python
from state_engine.engine import StateEngine

# Sample input lines
input_lines = [
    "error: disk full",
    "warn: low memory",
    "hello world"
]

# Create and run the engine
engine = StateEngine("config.yaml")
engine.run(iter(input_lines))
```

## Configuration

The system is configured using a YAML file that defines the processor nodes:

```yaml
nodes:
  - tag: start
    type: state_engine.processors.start.tag_lines

  - tag: error
    type: state_engine.processors.filters.only_error

  - tag: warn
    type: state_engine.processors.filters.only_warn

  - tag: general
    type: state_engine.processors.formatters.snakecase

  - tag: end
    type: state_engine.processors.output.terminal
```

Each node has:

- **tag**: The identifier that routes lines to this processor
- **type**: Python module path to the processor function

## Extending

Create new processors by defining functions that:

1. Accept an iterator of (tag, line) tuples
2. Yield new (tag, line) tuples

Example:

```python
def uppercase_processor(lines):
    for _, line in lines:
        yield ("end", line.upper())
```

Add your processor to the configuration file to include it in the processing pipeline.

## Example Flow

Input: `"error: disk full"`

1. Tagged as `("error", "error: disk full")` by start processor
2. Processed by error filter: `("general", "ERROR DETECTED: error: disk full")`
3. Transformed to snake_case: `("end", "error_detected:_error:_disk_full")`
4. Output to terminal

Input: `"hello world"`

1. Tagged as `("general", "hello world")` by start processor
2. Transformed to snake_case: `("end", "hello_world")`
3. Output to terminal
