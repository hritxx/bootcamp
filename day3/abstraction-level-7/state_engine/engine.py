import yaml
from typing import Iterator, List, Dict, Any
from state_engine.processors.start import StartProcessor
from state_engine.processors.filters import FilterProcessor
from state_engine.processors.formatters import FormatterProcessor
from state_engine.processors.output import OutputProcessor

class StateEngine:
    def __init__(self, config_path: str, trace_enabled: bool = False):
        self.config_path = config_path
        self.trace_enabled = trace_enabled
        self.traces = [] if trace_enabled else None
        self.stats = {
            "processed": 0,
            "filtered_out": 0,
            "errors": 0,
            "warnings": 0,
            "normal": 0
        }
        

        with open(config_path) as f:
            self.config = yaml.safe_load(f)
            

        self.start_processor = StartProcessor(self.config.get("start", {}))
        self.filter_processor = FilterProcessor(self.config.get("filters", {}))
        self.formatter_processor = FormatterProcessor(self.config.get("formatters", {}))
        self.output_processor = OutputProcessor(self.config.get("output", {}))
        
    def run(self, input_stream: Iterator[str]):

        for line in input_stream:
            self.stats["processed"] += 1
            

            state = {"raw_input": line}
            
            if self.trace_enabled:
                trace = {"line": line, "steps": []}
                self.traces.append(trace)
            

            state = self.start_processor.process(state)
            if self.trace_enabled:
                trace["steps"].append({"processor": "start", "state": state.copy()})
            

            state = self.filter_processor.process(state)
            if self.trace_enabled:
                trace["steps"].append({"processor": "filter", "state": state.copy()})
            

            if state.get("filtered", False):
                self.stats["filtered_out"] += 1
                continue
                

            state = self.formatter_processor.process(state)
            if self.trace_enabled:
                trace["steps"].append({"processor": "formatter", "state": state.copy()})
            

            if "message_type" in state:
                if state["message_type"] == "error":
                    self.stats["errors"] += 1
                elif state["message_type"] == "warning":
                    self.stats["warnings"] += 1
                else:
                    self.stats["normal"] += 1
            

            self.output_processor.process(state)
            if self.trace_enabled:
                trace["steps"].append({"processor": "output", "state": state.copy()})