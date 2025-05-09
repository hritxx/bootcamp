from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from typing import List, Dict, Any, Optional

app = FastAPI(title="State Engine Dashboard")


_engine = None

def register_engine(engine):
    global _engine
    _engine = engine

@app.get("/", response_class=HTMLResponse)
def root():

    return """
    <html>
        <head>
            <title>State Engine Dashboard</title>
        </head>
        <body>
            <h1>State Engine Dashboard</h1>
            <ul>
                <li><a href="/traces">Traces</a> - View execution traces</li>
                <li><a href="/stats">Stats</a> - View processing metrics</li>
            </ul>
        </body>
    </html>
    """

@app.get("/traces")
def get_traces():

    if _engine is None:
        return {"error": "Engine not initialized"}
    
    if not hasattr(_engine, "traces") or not _engine.trace_enabled:
        return {"error": "Tracing is not enabled"}
    
    return {"traces": _engine.traces}

@app.get("/stats")
def get_stats():

    if _engine is None:
        return {"error": "Engine not initialized"}
    
    if not hasattr(_engine, "stats"):
        return {"error": "Stats not available"}
    
    return {"stats": _engine.stats}