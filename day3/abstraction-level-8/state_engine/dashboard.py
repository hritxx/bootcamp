from fastapi import FastAPI
from fastapi.responses import JSONResponse
import threading
import uvicorn

app = FastAPI()
engine = None  

@app.get("/stats")
def get_stats():
    return JSONResponse(content=engine.metrics)

@app.get("/trace")
def get_trace():
    return JSONResponse(content=list(engine.traces))

@app.get("/errors")
def get_errors():
    return JSONResponse(content=list(engine.errors))

def run_dashboard():
    try:
        uvicorn.run(app, host="0.0.0.0", port=8000)
    except OSError as e:
        if "address already in use" in str(e).lower():

            print("[WARNING] Port 8000 is already in use. Trying port 8001...")
            try:
                uvicorn.run(app, host="0.0.0.0", port=8001)
            except Exception as e2:
                print(f"[ERROR] Failed to start dashboard: {e2}")
        else:
            print(f"[ERROR] Failed to start dashboard: {e}")