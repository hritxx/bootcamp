# Python Basic Drill

This repository contains two Python packages demonstrating basic concepts:

1. **hello-world**: A library that provides a `say_hello` function and a CLI tool
2. **many-hellos**: A CLI application that uses the hello-world library

## Features Demonstrated

- Creating reusable Python libraries
- Building command-line interfaces with Typer
- Configuration management with YAML files
- Python logging
- Package publication to dev-PyPI
- Environment variable usage
- Module reuse across projects

## Getting Started

### Installing hello-world

```bash
cd hello-world
pip install -e .
```

### Installing many-hellos

```bash
cd many-hellos
pip install -e .
```

## Usage

### hello-world CLI

```bash
hello John
```

### many-hellos CLI

```bash
many-hellos John Jane Alex
```

## Configuration

The `say_hello` function uses a YAML config file to determine how many times to repeat the greeting.
Configuration is loaded from:

1. Current directory (`_config.yaml`)
2. Paths in `CONFIG_PATH` environment variable (colon-separated)
3. Default config shipped with the package
