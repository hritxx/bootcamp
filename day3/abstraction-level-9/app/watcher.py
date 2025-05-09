import time
import os
from app.processor import process_file

WATCH_DIR = "watch_dir/unprocessed"

def watch_directory():
    print(f"[~] Watching {WATCH_DIR} for files...")
    while True:
        files = os.listdir(WATCH_DIR)
        for file in files:
            full_path = os.path.join(WATCH_DIR, file)
            if os.path.isfile(full_path):
                process_file(full_path)
                os.remove(full_path)
        time.sleep(2)
