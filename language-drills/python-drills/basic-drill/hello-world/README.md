# Hello World

A simple Python library that provides a function to say hello and a CLI tool.

## Installation

```bash
pip install hello-world
```

## Usage

### As a library

```python
from hello_world import say_hello

greeting = say_hello("John")
print(greeting)  # Output: Hello, John!
```

### As a CLI tool

```bash
hello John
```

## Configuration

The `say_hello` function uses a YAML config file to determine how many times to repeat the greeting.

Configuration is loaded from:

1. `_config.yaml` in the current directory
2. Paths in `CONFIG_PATH` environment variable (colon-separated)
3. Default config shipped with the package

Example `_config.yaml`:

```yaml
num_times: 3
```
