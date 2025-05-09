import os
import shutil
import time
from pathlib import Path
import threading
import yaml
from state_engine.engine import StateEngine
from state_engine.dashboard import run_dashboard, app

WATCH_DIR = Path("watch_dir")
UNPROCESSED = WATCH_DIR / "unprocessed"
UNDERPROCESS = WATCH_DIR / "underprocess"
PROCESSED = WATCH_DIR / "processed"

def recover_files():
    for file in UNDERPROCESS.glob("*"):
        shutil.move(file, UNPROCESSED / file.name)

def process_file(file_path, engine: StateEngine):
    print(f"[INFO] Processing: {file_path.name}")
    with open(file_path) as f:
        lines = f.readlines()
        engine.run(lines)
    shutil.move(file_path, PROCESSED / file_path.name)

def monitor_folder(engine: StateEngine):
    while True:
        for file in UNPROCESSED.glob("*"):
            in_progress = UNDERPROCESS / file.name
            shutil.move(file, in_progress)
            try:
                process_file(in_progress, engine)
            except Exception as e:
                print(f"[ERROR] Failed: {file.name}: {e}")
                shutil.move(in_progress, UNPROCESSED / file.name)
        time.sleep(2)

def start_all():
    with open("dag_config.yaml") as f:
        config = yaml.safe_load(f)
    engine = StateEngine(config, trace_enabled=True)
    from state_engine import dashboard
    dashboard.engine = engine
    recover_files()
    threading.Thread(target=run_dashboard, daemon=True).start()
    monitor_folder(engine)

if __name__ == "__main__":
    start_all()