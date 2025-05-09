import importlib
import time
from collections import defaultdict, deque
from typing import Dict, Callable, Iterable, Tuple

class StateEngine:
    def __init__(self, config: Dict, trace_enabled: bool = False):
        self.config = config
        self.trace_enabled = trace_enabled
        self.metrics = defaultdict(lambda: {"count": 0, "time": 0.0, "errors": 0})
        self.traces = deque(maxlen=100)
        self.errors = deque(maxlen=100)
        self.tag_to_processor = self._load_processors()

    def _load_processors(self) -> Dict[str, Callable]:
        tag_to_processor = {}
        for tag, steps in self.config.items():
            processors = []
            for step in steps:
                module_name, func_name = step["processor"].rsplit(".", 1)
                module = importlib.import_module(module_name)
                func = getattr(module, func_name)
                processors.append((func, step["outputs"]))
            tag_to_processor[tag] = processors
        return tag_to_processor

    def run(self, lines: Iterable[str]):
        queue = deque([("start", line.strip(), ["start"]) for line in lines])

        while queue:
            tag, line, trace = queue.popleft()
            processors = self.tag_to_processor.get(tag, [])
            for func, outputs in processors:
                start_time = time.time()
                try:
                    results = func([line])
                    duration = time.time() - start_time
                    self.metrics[tag]["count"] += 1
                    self.metrics[tag]["time"] += duration
                    

                    for result_tag, result_line in results:
                        next_tag = outputs.get(result_tag)
                        if next_tag: 
                            new_trace = trace + [next_tag]
                            if self.trace_enabled:
                                self.traces.append({"trace": new_trace, "line": result_line})
                            queue.append((next_tag, result_line, new_trace))
                except Exception as e:
                    self.metrics[tag]["errors"] += 1
                    self.errors.append({"tag": tag, "line": line, "error": str(e)})