# State Engine Dashboard

A monitoring and debugging dashboard for a distributed state engine system. This dashboard provides real-time metrics, trace information, and error logs through a REST API.

## Features

- **Real-time metrics**: View performance metrics and system state through the `/stats` endpoint
- **Trace monitoring**: Access execution traces for debugging via the `/trace` endpoint
- **Error reporting**: View system errors through the `/errors` endpoint
- **Automatic port selection**: Failover to alternate port if primary port is unavailable

## Setup

### Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn

### Installation

```bash
pip install fastapi uvicorn
```

### Running the Dashboard

The dashboard can be started by importing and using the `run_dashboard` function:

```python
from state_engine.dashboard import run_dashboard, engine
from your_state_engine import StateEngine

# Initialize your state engine
my_engine = StateEngine()

# Connect the dashboard to your engine
engine = my_engine

# Run the dashboard in a separate thread
import threading
dashboard_thread = threading.Thread(target=run_dashboard, daemon=True)
dashboard_thread.start()

# Your main application continues...
```

## API Endpoints

### GET /stats

Returns current metrics from the state engine.

Example response:

```json
{
  "processed_events": 1523,
  "average_processing_time_ms": 4.2,
  "active_workers": 8
}
```

### GET /trace

Returns a list of recent execution traces for debugging.

Example response:

```json
[
  {
    "timestamp": "2023-06-12T15:23:45",
    "event": "process_start",
    "data": { "event_id": "abc123" }
  },
  {
    "timestamp": "2023-06-12T15:23:46",
    "event": "process_complete",
    "data": { "event_id": "abc123", "duration_ms": 212 }
  }
]
```

### GET /errors

Returns a list of recent errors encountered by the state engine.

Example response:

```json
[
  {
    "timestamp": "2023-06-12T14:35:12",
    "error_type": "ConnectionError",
    "message": "Failed to connect to worker node"
  },
  {
    "timestamp": "2023-06-12T14:42:08",
    "error_type": "TimeoutError",
    "message": "Processing timed out after 30s"
  }
]
```

## Port Configuration

By default, the dashboard runs on port 8000. If this port is unavailable, it will automatically attempt to use port 8001.

## Integration

To integrate this dashboard with your state engine, ensure your engine implementation exposes the following properties:

- `metrics`: A dictionary containing current system metrics
- `traces`: An iterable collection of trace events
- `errors`: An iterable collection of error records

## License

MIT
