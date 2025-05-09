import importlib
import yaml
from typing import List, Dict, Any, Optional

from processor_types import StreamProcessor, ProcessorFn
from adapter import adapt_processor

def load_processor(processor_spec: Dict[str, Any]) -> StreamProcessor:

    processor_type = processor_spec["type"]
    config = processor_spec.get("config", {})
    

    module_path, func_name = processor_type.rsplit(".", 1)
    
    try:
        module = importlib.import_module(module_path)
        processor_factory = getattr(module, func_name)
        
        
        if callable(processor_factory) and hasattr(processor_factory, "__annotations__"):

            if processor_factory.__annotations__.get("return") == str:
                return adapt_processor(processor_factory)
        

        if config:

            return processor_factory(config)
        else:

            return processor_factory()
            
    except (ImportError, AttributeError) as e:
        raise ImportError(f"Could not import {processor_type}: {e}")

def load_pipeline(config_path: str) -> List[StreamProcessor]:

    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    steps = config.get("pipeline", [])
    pipeline = []

    for step in steps:
        processor = load_processor(step)
        pipeline.append(processor)

    return pipeline
