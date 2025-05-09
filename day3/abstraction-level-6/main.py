from state_engine.engine import StateEngine

if __name__ == "__main__":
    sample_input = [
        "   error: disk full",
        "warn: low memory",
        "hello world",
        "   ERROR: crash",
        "warn: cpu hot"
    ]
    engine = StateEngine("config.yaml")
    engine.run(iter(sample_input))