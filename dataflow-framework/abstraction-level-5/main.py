from dag_engine.engine import DAGEngine

if __name__ == "__main__":
    sample_input = [
        "   error: disk full",
        "warn: low memory",
        "hello world",
        "   ERROR: crash",
        "warn: cpu hot"
    ]
    engine = DAGEngine("dag_engine/config.yaml")
    engine.run(iter(sample_input))