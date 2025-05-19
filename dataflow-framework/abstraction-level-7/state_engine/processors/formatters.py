from typing import Dict, Any
import re

class FormatterProcessor:
   
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.uppercase = config.get("uppercase", False)
        
    def process(self, state: Dict[str, Any]) -> Dict[str, Any]:
        
        cleaned_input = state.get("cleaned_input", "")
        

        if self.uppercase:
            formatted_message = cleaned_input.upper()
        else:
            formatted_message = cleaned_input
            
        state["formatted_message"] = formatted_message
        

        message_type = state.get("initial_type", "info")
        

        if message_type == "error":
            content = re.sub(r'(?i)^error\s*:\s*', '', formatted_message)
            state["message_type"] = "error"
            state["severity"] = "high"
        elif message_type == "warning":
            content = re.sub(r'(?i)^warn(?:ing)?\s*:\s*', '', formatted_message)
            state["message_type"] = "warning"
            state["severity"] = "medium"
        else:
            content = formatted_message
            state["message_type"] = "info"
            state["severity"] = "low"
            
        state["message_content"] = content
        
        return state