from typing import Dict, Any, Optional

def contains_filter(text: str, config: Dict[str, Any]) -> Optional[str]:
    """Filter text based on whether it contains specified substring."""
    substring = config.get("contains", "")
    invert = config.get("invert", False)
    
    contains = substring in text
    if invert:
        contains = not contains
    
    return text if contains else None

def length_filter(text: str, config: Dict[str, Any]) -> Optional[str]:
    """Filter text based on length constraints."""
    min_length = config.get("min_length", 0)
    max_length = config.get("max_length", float('inf'))
    
    text_length = len(text)
    if text_length >= min_length and text_length <= max_length:
        return text
    return None

def regex_filter(text: str, config: Dict[str, Any]) -> Optional[str]:
    """Filter text based on regex pattern."""
    import re
    pattern = config.get("pattern", ".*")
    invert = config.get("invert", False)
    
    matches = bool(re.search(pattern, text))
    if invert:
        matches = not matches
    
    return text if matches else None
