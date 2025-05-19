# Text Processor - Abstraction Level 2

## Overview

This is a text processing utility demonstrating abstraction level 2. The program processes input text through a configurable pipeline of transformation functions and outputs the result to either a file or standard output.

## How It Works

The text processor introduces a more modular architecture with:

1. **Core Processing Logic**: Separate modules for core text transformations and processing
2. **Pipeline Architecture**: Transformations are organized as a pipeline of processor functions
3. **Configuration System**: Processing mode selection via environment variables or CLI arguments
4. **Abstracted I/O**: File reading and writing are handled through dedicated functions
5. **Type Definitions**: Custom type definitions for better code organization and clarity

## Abstraction Level 2

This represents the second level of abstraction where:

- Code is organized into separate modules with specific responsibilities:
  - `core.py`: Core transformation functions and pipeline processing
  - `pipeline.py`: Pipeline configuration and processor selection
  - `main.py`: Application logic for file handling and orchestration
  - `cli.py`: Command-line interface implementation
  - `processor_types.py`: Type definitions for processor functions
- Processing functions are selected dynamically based on configuration
- Type hints are used for better code clarity and IDE support
- The dotenv library manages environment configuration

This modular design improves maintainability and makes extending the functionality easier.

## Usage

```bash
# Basic usage (using default mode from environment)
python -m cli process input.txt

# Specifying output file
python -m cli process input.txt --output output.txt

# Specifying processing mode
python -m cli process input.txt --mode snakecase
```

## Environment Configuration

You can set the default processing mode in the `.env` file:

```
MODE=uppercase
# or
MODE=snakecase
```

## Architecture

The application follows a modular architecture:

1. **CLI Layer**: Handles command-line arguments and environment setup
2. **Main Layer**: Orchestrates file I/O and pipeline execution
3. **Pipeline Layer**: Configures the processing pipeline based on the selected mode
4. **Core Layer**: Contains the actual text transformation functions and pipeline execution

## Available Processing Modes

- `uppercase`: Converts text to UPPERCASE
- `snakecase`: Converts text to snake_case (lowercase with underscores)

## Requirements

- Python 3.6+
- typer
- python-dotenv
