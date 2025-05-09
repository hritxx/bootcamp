import importlib
import yaml
from typing import Iterator, Tuple, Dict, Callable
from collections import deque

Line = str
TaggedLine = Tuple[str, Line]
Processor = Callable[[Iterator[TaggedLine]], Iterator[TaggedLine]]

class StateEngine:
    def __init__(self, config_path: str):
        with open(config_path) as f:
            config = yaml.safe_load(f)
        
        self.tag_to_processor = {}

        for node in config["nodes"]:
            tag = node["tag"]
            module_path, func_name = node["type"].rsplit(".", 1)
            mod = importlib.import_module(module_path)
            processor = getattr(mod, func_name)
            self.tag_to_processor[tag] = processor

    def load_processors(self, nodes_config):
        for node in nodes_config:
            tag = node["tag"]
            module_path, func_name = node["type"].rsplit(".", 1)
            mod = importlib.import_module(module_path)
            self.processors[tag] = getattr(mod, func_name)

    def run(self, input_lines: Iterator[str]):
        queue = [("start", line) for line in input_lines]

        while queue:
            tag, line = queue.pop(0)
            print(f"[DEBUG] Processing tag={tag}, line={line!r}")  # 🪵 DEBUG LINE
            if tag == "end":
                continue
            processor = self.tag_to_processor.get(tag)
            if not processor:
                raise ValueError(f"No processor found for tag '{tag}'")
            for new_tag, new_line in processor([(tag, line)]):
                print(f"[DEBUG] → Emitting tag={new_tag}, line={new_line!r}")  # 🪵 DEBUG LINE
                queue.append((new_tag, new_line))