import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log", 
)

logger = logging.getLogger(__name__)

debug_mode = True

def greet_user(user):
    if debug_mode:
        logger.debug(f"Greeting user: {user}")
    logger.info(f"Hello, {user}!")

greet_user("Alice")