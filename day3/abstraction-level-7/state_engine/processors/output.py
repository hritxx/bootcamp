from typing import Dict, Any

class OutputProcessor:

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.console_output = config.get("console_output", True)
        self.add_prefix = config.get("add_prefix", True)
        
    def process(self, state: Dict[str, Any]) -> Dict[str, Any]:

        if state.get("filtered", False):
            return state
            
        message_type = state.get("message_type", "info")
        message_content = state.get("message_content", "")
        

        if self.add_prefix:
            if message_type == "error":
                prefix = "[ERROR] "
            elif message_type == "warning":
                prefix = "[WARNING] "
            else:
                prefix = "[INFO] "
                
            output_text = f"{prefix}{message_content}"
        else:
            output_text = message_content
            
        state["output_text"] = output_text
        

        if self.console_output:
            print(output_text)
            
        return state