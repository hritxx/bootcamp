import importlib
import yaml
from processor_types import ProcessorFn

def load_pipeline(config_path: str) -> list[ProcessorFn]:
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    steps = config.get("pipeline", [])
    pipeline = []

    for step in steps:
        import_path = step["type"]
        module_path, func_name = import_path.rsplit(".", 1)
        try:
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
            pipeline.append(func)
        except (ImportError, AttributeError) as e:
            raise ImportError(f"Could not import {import_path}: {e}")

    return pipeline