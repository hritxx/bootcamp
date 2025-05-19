# Text Processor - Abstraction Level 3

## Overview

This is a text processing utility demonstrating abstraction level 3. The program processes input text through a dynamically loaded pipeline of transformation processors defined in YAML configuration, providing maximum flexibility and extensibility.

## How It Works

The text processor implements a sophisticated architecture with:

1. **Dynamic Module Loading**: Processors are loaded dynamically from modules based on configuration
2. **YAML Configuration**: Pipeline steps are defined in a YAML file
3. **Modular Processors**: Text processors are organized in a dedicated package structure
4. **Type Annotations**: Comprehensive type annotations for enhanced code clarity and IDE support
5. **Environment Variable Support**: Configuration can be influenced by environment variables
6. **CLI Interface with Typer**: Full-featured command-line interface with help text and options

## Abstraction Level 3

This represents the third level of abstraction where:

- Code is organized into a clear package structure:
  - `processors/`: A package containing individual processor modules
  - `pipeline.py`: Handles dynamic loading of processors based on YAML config
  - `processor_types.py`: Type definitions for the processor functions
  - `core.py`: Core logic for applying the processor pipeline
  - `main.py`: Application orchestration and file handling
  - `cli.py`: Command-line interface implementation
- Configuration is fully externalized to YAML files
- Processors are dynamically loaded using Python's importlib
- Error handling for import failures provides better debugging
- Proper typing is used throughout for better code clarity

This design provides maximum flexibility to add new processors without modifying the core application code.

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
  - type: processors.upper.to_uppercase
```

Each entry in the pipeline specifies:

- `type`: The fully qualified import path to the processor function

## Adding New Processors

To add a new processor:

1. Create a new Python file in the `processors` package
2. Define a function that takes a string and returns a transformed string
3. Add the processor to your pipeline.yaml configuration

For example, to add a "title case" processor:

```python
# processors/title.py
def to_titlecase(line: str) -> str:
    return line.title()
```

Then update your configuration:

```yaml
pipeline:
  - type: processors.snake.to_snakecase
  - type: processors.title.to_titlecase
```

## Environment Configuration

Environment variables can be set in the `.env` file and are loaded automatically:

```
MODE=uppercase
```

## Requirements

- Python 3.6+
- typer
- python-dotenv
- pyyaml
