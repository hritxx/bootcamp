import sys
import yaml
import time
from state_engine.engine import StateEngine
from state_engine.dashboard import run_dashboard
import threading
import signal

def timeout_handler(signum, frame):
    print("Processing timed out! Possible infinite loop detected.")
    sys.exit(1)


def load_config(config_path="dag_config.yaml"):
    with open(config_path) as f:
        return yaml.safe_load(f)

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file> [--trace]")
        sys.exit(1)

    input_file = sys.argv[1]
    trace_enabled = "--trace" in sys.argv

    config = load_config()
    engine = StateEngine(config, trace_enabled=trace_enabled)


    from state_engine import dashboard
    dashboard.engine = engine


    dashboard_thread = threading.Thread(target=run_dashboard, daemon=True)
    dashboard_thread.start()


    with open(input_file) as f:
        lines = f.readlines()
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(30)  
       
        try:
            engine.run(lines)
            signal.alarm(0) 
        except Exception as e:
            print(f"Error during processing: {e}")

    print("[INFO] Processing complete. Visit http://localhost:8000/stats for live metrics.")
    

    print("[INFO] Press Ctrl+C to exit and terminate the dashboard")
    try:

        while dashboard_thread.is_alive():
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[INFO] Exiting...")
        sys.exit(0)

    

if __name__ == "__main__":
    main()
