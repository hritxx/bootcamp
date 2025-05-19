from typing import Dict, Any

class FilterProcessor:

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.exclude_empty = config.get("exclude_empty", True)
        self.only_errors = config.get("only_errors", False)
        self.only_warnings = config.get("only_warnings", False)
        
    def process(self, state: Dict[str, Any]) -> Dict[str, Any]:

        if self.exclude_empty and state.get("empty", False):
            state["filtered"] = True
            state["filter_reason"] = "empty_message"
            return state
            

        if self.only_errors and state.get("initial_type") != "error":
            state["filtered"] = True
            state["filter_reason"] = "not_error"
            return state
            
        if self.only_warnings and state.get("initial_type") != "warning":
            state["filtered"] = True
            state["filter_reason"] = "not_warning"
            return state
            

        state["filtered"] = False
        return state