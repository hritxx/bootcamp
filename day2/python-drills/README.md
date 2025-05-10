# Python Drills - Day 2

This repository contains my work from Day 2 of the Python bootcamp, where I practiced fundamental Python concepts through hands-on drills. These exercises helped me understand idiomatic Python and build practical skills in creating reusable components.

## Basic Drills Completed

During Day 2, I worked through a series of drills to understand proper Python project workflows:

### 1. Hello World Package

- Created a reusable Python library with a `say_hello` function
- Implemented a command-line interface using Typer
- Published the package to dev-PyPI

### 2. Many-Hellos Application

- Built a second CLI application that imports and uses the hello-world library
- Demonstrated effective module reuse across projects

### 3. Configuration Management

- Extended the `say_hello` function to use YAML configuration files
- Implemented a hierarchical config lookup system:
  - Current directory (`_config.yaml`)
  - Paths from `CONFIG_PATH` environment variable
  - Default config shipped with the package

### 4. Logging Implementation

- Added Python's standard logging to both projects
- Created configurable logging levels
- Demonstrated selective logging for specific components

## Project Structure

This repository contains two main packages:

```
python-drills/
├── basic-drill/
│   ├── hello-world/       # Core library package
│   └── many-hellos/       # Application that uses hello-world
└── README.md
```

## Key Skills Practiced

- ✅ Creating modular, reusable Python libraries
- ✅ Building CLI applications with Typer
- ✅ Package publishing workflow
- ✅ Configuration management with YAML
- ✅ Environment variable usage
- ✅ Cross-package module reuse
- ✅ Implementing proper logging

## Getting Started

See the individual project READMEs for installation and usage instructions:

- [Basic Drill README](./basic-drill/README.md)
