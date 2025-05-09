# Text Processor - Abstraction Level 0

## Overview

This is a simple text processing utility that demonstrates the most basic level of abstraction (Level 0). The program reads input from standard input (stdin), strips whitespace, converts the text to uppercase, and outputs the result.

## How It Works

The `process.py` script:

1. Reads input line by line from stdin
2. Strips any leading/trailing whitespace from each line
3. Converts each line to uppercase
4. Prints the processed line to stdout

## Usage

Run the script by piping text into it:

```bash
echo "hello world" | python process.py
# Output: HELLO WORLD

# Or using a file:
cat input.txt | python process.py
```

## Abstraction Level 0

This represents the lowest level of abstraction where the processing logic is explicitly written in the main script without any:

- Functions
- Classes
- Modules
- Configuration files

The purpose is to demonstrate the most basic form of a text processing program before introducing higher levels of abstraction in subsequent examples.
