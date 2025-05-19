# DAG Engine - Abstraction Level 5

## Overview

This project implements a Directed Acyclic Graph (DAG) processing engine for text streams. The DAG Engine represents the fifth level of abstraction in our text processing journey, introducing dynamic routing of data through processor nodes based on tags and configured routes.

## Key Features

- **Dynamic Data Routing**: Process data through different paths based on tags
- **Configurable Processing Graph**: Define processor nodes and their connections via YAML
- **Pluggable Processor Architecture**: Easily extend with new processor types
- **Line Tagging System**: Lines are tagged to determine their processing path
- **Fan-out & Fan-in Support**: One input can branch to multiple processors, and multiple inputs can converge
- **Dynamic Module Loading**: Processors are loaded at runtime based on configuration

## How It Works

The DAG Engine works by:

1. **Reading Configuration**: Loading node definitions and route mappings from a YAML file
2. **Creating Processor Graph**: Building a graph of processor nodes and connections
3. **Processing Data**:
   - Each data item is tagged with its current position in the graph
   - Processors transform data and assign new tags
   - Tags determine the next processor(s) in the pipeline
4. **Routing**: The engine routes data through the graph based on tags and defined routes

## Architecture

### Components

- **DAGEngine**: Main engine class that loads config and processes data
- **Processors**: Individual functions that receive data and yield processed results with new tags
- **Graph Configuration**: YAML file defining nodes and routes

### Data Flow

```
[Input] --> [start] --> [trim] --> [tagger] --+--> [error] --> [end]
                                             |
                                             +--> [warn] --> [end]
                                             |
                                             +--> [general] --> [end]
```

## Configuration

The engine is configured through a YAML file:

```yaml
nodes:
  - tag: start
    type: dag_engine.processors.start.emit_lines
  - tag: trim
    type: dag_engine.processors.trim.trim
  # ...more nodes...

routes:
  start: [trim]
  trim: [tagger]
  tagger:
    error: [error]
    warn: [warn]
    general: [general]
  # ...more routes...
```

### Node Definition

Each node has:

- `tag`: Identifier for this processor
- `type`: Import path to the processor function

### Route Definition

Routes define the connections between nodes:

- Simple routes: `source: [destination1, destination2]`
- Conditional routes: `source: {tag1: [dest1], tag2: [dest2]}`

## Usage

```python
from dag_engine.engine import DAGEngine

# Create engine with configuration
engine = DAGEngine("path/to/config.yaml")

# Process data
input_lines = ["error: disk full", "hello world", "warn: low memory"]
engine.run(iter(input_lines))
```

## Adding New Processors

1. Create a processor function in the `dag_engine/processors/` directory:

```python
def my_processor(lines):
    for line in lines:
        # Process the line
        processed_line = line.upper()
        # Yield with a tag to determine the next processor
        yield ("next_tag", processed_line)
```

2. Add the processor to your configuration:

```yaml
nodes:
  - tag: my_tag
    type: dag_engine.processors.mymodule.my_processor

routes:
  # Connect your processor to the graph
  some_previous_node: [my_tag]
  my_tag: [some_next_node]
```

## Requirements

- Python 3.6+
- PyYAML

## Examples

See `main.py` for a complete example that processes a list of log lines, routing them differently based on their content.

## Abstraction Level

This represents the fifth level of abstraction where:

- Data is processed through a dynamic processing graph
- Routes are determined at runtime based on tags
- The system handles complex branching and merging of data streams
- Configuration defines both processors and connections between them
