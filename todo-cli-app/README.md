# 📝 Todo CLI App

A simple command-line To-Do list manager built with Python and managed using [uv](https://github.com/astral-sh/uv).

---

## 🚀 Purpose

This project helps users manage daily tasks from the command line. It's beginner-friendly and demonstrates:

- Argument parsing with `argparse`
- JSON-based file storage
- Modern dependency management using `uv`

---

## ⚙️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/hritxx/bootcamp.git
cd bootcamp/todo-cli-app
```

2. **Install the package:**

```bash
# Using uv (recommended)
uv pip install -e .

# Using pip
pip install -e .
```

3. **Verify installation:**

```bash
todo --help
```

---

## 🛠️ Usage

The Todo CLI App provides several commands to manage your tasks:

### List all tasks

```bash
todo list
```

Output example:

```
1. ❌ Write documentation
2. ❌ Try uv for dependency management
```

### Add a new task

```bash
todo add "Your task description"
```

Output example:

```
✅ Added task: Your task description
```

### Mark a task as done

```bash
todo done 1
```

Output example:

```
✅ Marked task 1 as done.
```

When you list the tasks again, you'll see the status updated:

```
1. ✅ Write documentation
2. ❌ Try uv for dependency management
```

---

## 📂 Project Structure

```
todo-cli-app/
├── todo/               # Main package directory
│   ├── __init__.py     # Package initialization
│   └── main.py         # Core functionality
├── tests/              # Test directory
│   └── test_basic.py   # Basic tests
├── tasks.json          # Task storage file
├── pyproject.toml      # Project configuration
├── README.md           # Documentation
└── .gitignore          # Git ignore rules
```

---

## 🧪 Testing

Run the tests with:

```bash
pytest
```

---

## 🛠️ Development

### Setting up a development environment

1. Create a virtual environment:

```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install in development mode:

```bash
uv pip install -e .
```

### Running the application in development

After installing in development mode, you can run the application with:

```bash
todo <command>
```

Any changes you make to the code will be immediately available when you run the command.

---

## 📋 Roadmap

Future features we're considering:

- [ ] Task deletion
- [ ] Task editing
- [ ] Priority levels for tasks
- [ ] Due dates
- [ ] Categories/tags for tasks
- [ ] Interactive mode

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.
