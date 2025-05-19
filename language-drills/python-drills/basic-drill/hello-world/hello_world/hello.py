import logging
from .config_loader import load_config


logger = logging.getLogger(__name__)

def say_hello(name):
    logger.debug(f"Saying hello to {name}")
    
    config = load_config()
    num_times = config.get('num_times', 1)
    
    logger.info(f"Repeating hello {num_times} times as per config")
    
    greeting = f"Hello, {name}! " * num_times
    return greeting.strip()
