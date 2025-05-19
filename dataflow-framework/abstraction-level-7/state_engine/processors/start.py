from typing import Dict, Any

class StartProcessor:

    def __init__(self, config: Dict[str, Any]):
        self.config = config
    
    def process(self, state: Dict[str, Any]) -> Dict[str, Any]:

        raw_input = state.get("raw_input", "")
        

        cleaned_input = raw_input.strip()
        state["cleaned_input"] = cleaned_input
        

        if not cleaned_input:
            state["empty"] = True
            return state
            

        if "error:" in cleaned_input.lower():
            state["initial_type"] = "error"
        elif "warn:" in cleaned_input.lower():
            state["initial_type"] = "warning"
        else:
            state["initial_type"] = "info"
            
        return state