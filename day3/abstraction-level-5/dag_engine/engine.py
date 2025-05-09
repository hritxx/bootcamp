import importlib
import yaml
from typing import Iterator, Tuple, Dict, Callable

Line = str
TaggedLine = Tuple[str, Line]

class DAGEngine:
    def __init__(self, config_path: str):
        with open(config_path) as f:
            config = yaml.safe_load(f)
        self.graph = config["routes"]
        self.nodes = self.load_nodes(config["nodes"])

    def load_nodes(self, nodes_config):
        processors = {}
        for node_config in nodes_config:
            tag = node_config["tag"]
            module_path, func_name = node_config["type"].rsplit(".", 1)
            mod = importlib.import_module(module_path)
            processors[tag] = getattr(mod, func_name)
        return processors

    def run(self, input_lines: Iterator[Line]):
        queue: list[TaggedLine] = [("start", line) for line in input_lines]

        while queue:
            tag, line = queue.pop(0)
            if tag == "end":
                continue
            processor = self.nodes[tag]
            for new_tag, new_line in processor([line]):
                if new_tag in self.graph.get(tag, []):
                    queue.append((new_tag, new_line))