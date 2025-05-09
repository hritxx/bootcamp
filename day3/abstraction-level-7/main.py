import typer
import threading
import uvicorn
from dashboard.api import app as api_app, register_engine
from state_engine.engine import StateEngine

cli = typer.Typer()

@cli.callback(invoke_without_command=True)
def main(trace: bool = typer.Option(False, "--trace", help="Enable tracing")):
    print(f"Starting engine with tracing={'enabled' if trace else 'disabled'}")
    engine = StateEngine("config.yaml", trace_enabled=trace)
    register_engine(engine)

    print("Starting dashboard on http://127.0.0.1:8000")
    dashboard_thread = threading.Thread(target=lambda: uvicorn.run(api_app, host="127.0.0.1", port=8000), daemon=True)
    dashboard_thread.start()

    print("Processing sample input...")
    sample_input = [
        "   error: disk full",
        "warn: low memory",
        "hello world",
        "   ERROR: crash",
        "warn: cpu hot"
    ]
    engine.run(iter(sample_input))
    
    print("Processing complete. Dashboard is running. Press Ctrl+C to exit.")
    try:
        while True:
            import time
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down...")

if __name__ == "__main__":
    cli()