import os
import yaml
import logging
from pathlib import Path
import importlib.resources as pkg_resources


logger = logging.getLogger(__name__)

def load_config():
    current_dir_config = Path('./_config.yaml')
    if current_dir_config.exists():
        logger.info(f"Loading config from current directory: {current_dir_config}")
        with open(current_dir_config, 'r') as f:
            return yaml.safe_load(f)
    
    config_paths = os.environ.get('CONFIG_PATH', '')
    if config_paths:
        paths = config_paths.split(':')
        for path in paths:
            config_path = Path(path) / '_config.yaml'
            if config_path.exists():
                logger.info(f"Loading config from environment path: {config_path}")
                with open(config_path, 'r') as f:
                    return yaml.safe_load(f)

    logger.info("Using default config from package")
    try:
        with pkg_resources.open_text('hello_world', 'default_config.yaml') as f:
            return yaml.safe_load(f)
    except Exception as e:
        logger.warning(f"Failed to load default config: {e}")
        return {'num_times': 1}
