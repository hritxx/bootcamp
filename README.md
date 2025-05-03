# 🎉 Hriteek Hello

[![PyPI version](https://img.shields.io/pypi/v/hriteek-hello.svg)](https://pypi.org/project/hriteek-hello/)
[![Python Versions](https://img.shields.io/pypi/pyversions/hriteek-hello.svg)](https://pypi.org/project/hriteek-hello/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> Say hello with style - A simple yet elegant greeting package for your Python projects.

## ✨ Features

- 🖨️ Beautiful, colorful terminal output using Rich
- 🎯 Simple command-line interface with Typer
- 🔧 Customizable greetings with name options
- 🚀 Easy to use both as a library and command-line tool

## 🚀 Installation

```bash
pip install -i https://test.pypi.org/simple/ hriteek-hello
```

## 🧩 Usage

### As a Command Line Tool

```bash
# Default greeting
hriteek-hello greet

# Greeting with a name
hriteek-hello greet --name "Hriteek"
```

### As a Python Library

```python
from hriteek_hello.hello import say_hello

# Default greeting
say_hello()

# Greeting with a name
say_hello("Hriteek")
```

## 🎬 Demo

Watch the package in action:

[![asciicast](https://asciinema.org/a/ZGNoWlYfwb2hgnEbqBvwEr8sZ.svg)](https://asciinema.org/a/ZGNoWlYfwb2hgnEbqBvwEr8sZ)

## 📘 API Reference

### `say_hello(name: Optional[str] = None) -> None`

Displays a stylized greeting message.

**Parameters:**

- `name` (optional): The name to greet. Defaults to "World" if not provided.

**Example:**

```python
from hriteek_hello.hello import say_hello

# Will print: Hello, World!
say_hello()

# Will print: Hello, Hriteek!
say_hello("Hriteek")
```

## 🔧 Development

To set up the development environment:

1. Clone the repository:

   ```bash
   git clone https://github.com/hritxx/hriteek-hello.git
   cd hriteek-hello
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📬 Contact

Hriteek Roy - [@hritxx](https://github.com/hritxx) - hriteekroy1869@gmail.com

Project Link: [https://github.com/hritxx/hriteek-hello](https://github.com/hritxx/hriteek-hello)
