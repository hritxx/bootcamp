# Real-Time File Processing System Evolution

This project demonstrates the evolution of a text processing system through increasing levels of abstraction, from a simple script to a distributed, observable state engine. Each level builds upon the previous one, introducing new concepts and architectural improvements.

## 📊 Abstraction Levels

### Level 1: Basic Parameterization

- Simple text processing with configurable modes (uppercase, snakecase)
- Command-line interface with typer
- Environment variable configuration via python-dotenv
- Function-based organization within a single file

### Level 2: Modular Architecture

- Separation of concerns across multiple modules
- Pipeline architecture with `str -> str` processors
- Type definitions for better code clarity
- Dynamic processor selection based on configuration

### Level 3: Dynamic Configuration

- YAML-based pipeline configuration
- Dynamic module loading via importlib
- Organized package structure
- Fully decoupled processing logic from code

### Level 4: Stream Processing

- Evolution to `Iterator[str] -> Iterator[str]` processors
- Support for stateful operations (counters, buffers)
- Fan-in/fan-out capabilities (combining/splitting lines)
- Backward compatibility via adapters for simple processors

### Level 5: DAG-Based Routing

- Dynamic routing of data through processor nodes
- Tag-based flow control
- Configurable graph structure via YAML
- Support for conditional processing paths

### Level 6: State-Based Routing

- General-purpose state transition engine
- Lines carrying tags to determine processing flow
- Support for complex workflows including loops
- Decoupling of routing logic from processor implementation

### Level 7: Observability

- Real-time metrics collection
- Execution tracing for debugging
- FastAPI-based dashboard on separate thread
- Monitoring of system performance and health

### Level 8: Automated Processing

- Continuous folder monitoring for new files
- Three-directory queue pattern (unprocessed/underprocess/processed)
- Automatic recovery after system crashes
- Live dashboard showing processing state

### Level 9: Production-Ready System

- Dual execution modes (one-shot and watch)
- Docker containerization
- File upload via HTTP and rsync
- Comprehensive documentation and deployment guides

## 🚀 Key Features

- **Tag-Based Routing**: Flexible processing paths based on content
- **Stream-Based Processing**: Efficient handling of large files
- **Observable State**: Real-time metrics and tracing
- **Fault Tolerance**: Automatic recovery from failures
- **Configurable Pipeline**: No code changes needed for new workflows
- **Modular Design**: Easy to extend with new processors

## 📈 Architecture Evolution

The system evolved from a simple line-by-line processor to a distributed, observable state engine, with each abstraction level introducing important concepts:

1. **Function Organization** → **Modular Structure** → **Dynamic Loading**
2. **String Processors** → **Stream Processors** → **Stateful Processors**
3. **Linear Pipeline** → **Directed Graph** → **State Machine**
4. **Single File** → **Multiple Files** → **Continuous Processing**
5. **Basic Output** → **Metrics Collection** → **Real-Time Dashboard**

## 🔧 Running the System

See individual level READMEs for specific instructions. The final system (Level 9) supports:

```bash
# One-shot processing
python main.py --input somefile.txt

# Continuous monitoring
python main.py --watch
```

## 📋 Requirements

- Python 3.6+
- FastAPI
- Uvicorn
- PyYAML
- Typer
- python-dotenv

## 🎓 Lessons Learned

This project demonstrates how abstraction evolves naturally when solving increasingly complex problems. The key insights include:

- **Decoupling Configuration**: Separating what from how enables flexibility
- **Stream Processing**: Working with iterators enables powerful transformations
- **State Management**: Explicit state tracking supports complex workflows
- **Observability**: Real-time insight is critical for operational systems
- **Resilience Patterns**: Folder-based queues provide durability and recovery
