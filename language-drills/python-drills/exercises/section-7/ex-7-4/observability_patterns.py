import logging
import time
import os
import psutil

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
DEBUG = True

def log_with_context(user_id, func_name, msg):
    if DEBUG:
        logging.debug(f"[{user_id}] [{func_name}] {msg}")

def timed_function():
    start = time.time()
    time.sleep(0.3)
    duration = time.time() - start
    logging.info(f"Function duration: {duration:.3f}s")
    return duration

def health_check():
    return {"status": "ok", "uptime": time.time()}

def print_resource_usage():
    print("CPU Load:", os.getloadavg())
    print("Memory (MB):", psutil.virtual_memory().used / (1024*1024))


def trace(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with {args}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return wrapper

@trace
def add(a, b):
    return a + b

log_with_context("user123", "main", "Started script")
timed_function()
print_resource_usage()
print(health_check())
add(10, 5)