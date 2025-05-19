# Text Processor - Abstraction Level 1

## Overview

This is a text processing utility demonstrating abstraction level 1. The program processes text by transforming it based on a specified mode (uppercase or snake_case) and writes the result to either standard output or a specified file.

## How It Works

The `process.py` script implements text processing with the following features:

1. **Input Handling**: Reads text from a specified input file
2. **Processing Modes**:
   - `uppercase` - Converts text to UPPERCASE
   - `snakecase` - Converts text to snake_case (lowercase with underscores)
3. **Output Options**: Writes to a specified file or to stdout if no output file is specified
4. **Configuration via Environment**: Can read the processing mode from an environment variable

## Abstraction Level 1

This represents the first level of abstraction where:

- The code is organized into functions with specific responsibilities
- Configuration can come from environment variables or command-line arguments
- The dotenv library is used for environment variable management
- Command-line interface is built using the Typer library

This design separates the processing logic into discrete functions, making the code more modular compared to level 0.

## Usage

```bash
# Basic usage (using default mode from environment)
python process.py input.txt

# Specifying output file
python process.py input.txt --output output.txt

# Specifying processing mode
python process.py input.txt --mode snakecase

# Specifying both
python process.py input.txt --output output.txt --mode uppercase
```

## Environment Configuration

You can set the default processing mode in the `.env` file:

```
MODE=uppercase
# or
MODE=snakecase
```

## Function Overview

- `read_lines()` - Reads lines from the input file
- `transform_line()` - Applies the specified transformation to a line
- `write_output()` - Writes processed lines to the output destination
- `process()` - Main command function that orchestrates the processing

## Requirements

- Python 3.6+
- typer
- python-dotenv
