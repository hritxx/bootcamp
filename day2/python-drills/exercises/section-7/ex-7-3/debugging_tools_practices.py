import pdb
import traceback
import warnings
import logging

logging.basicConfig(level=logging.DEBUG)

def buggy_function(x):
    try:
        result = 10 / x
        return result
    except Exception as e:
        print("Verbose Exception:", type(e), e)
        print(traceback.format_exc())
        raise

def recurse(n, level=0):
    logging.debug(f"Recurse level {level}")
    if n == 0:
        return 1
    return n * recurse(n - 1, level + 1)


warnings.warn("This is a warning, not an error")


print(buggy_function(0))