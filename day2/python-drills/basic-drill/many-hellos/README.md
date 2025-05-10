# Many Hellos

A CLI tool that uses the hello-world library to greet multiple people.

## Installation

```bash
pip install many-hellos
```

## Usage

```bash
many-hellos John Jane Alex
```

## Logging Options

- `--verbose` or `-v`: Enable detailed logging for all components
- `--config-only` or `-c`: Only log configuration loading messages

## Configuration

This tool uses the configuration system from hello-world library.

You can influence the greeting behavior by:

1. Creating a `_config.yaml` file in the current directory
2. Setting the `CONFIG_PATH` environment variable
3. Relying on the default configuration

Example `_config.yaml`:

```yaml
num_times: 3
```
