import time
import threading
from collections import defaultdict, deque

class Metrics:
    def __init__(self, max_traces=1000, max_errors=100):
        self.lock = threading.Lock()
        self.processor_counts = defaultdict(int)
        self.processor_times = defaultdict(float)
        self.processor_errors = defaultdict(int)
        self.traces = deque(maxlen=max_traces)
        self.errors = deque(maxlen=max_errors)

    def record_start(self, processor_name):
        return time.time()

    def record_end(self, processor_name, start_time):
        elapsed = time.time() - start_time
        with self.lock:
            self.processor_counts[processor_name] += 1
            self.processor_times[processor_name] += elapsed

    def record_trace(self, trace):
        with self.lock:
            self.traces.append(trace)

    def record_error(self, processor_name, error_msg):
        with self.lock:
            self.processor_errors[processor_name] += 1
            self.errors.append({
                "processor": processor_name,
                "error": error_msg,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            })

    def get_stats(self):
        with self.lock:
            return {
                name: {
                    "count": self.processor_counts[name],
                    "total_time": round(self.processor_times[name], 4),
                    "errors": self.processor_errors[name]
                }
                for name in set(self.processor_counts) | set(self.processor_times) | set(self.processor_errors)
            }

    def get_traces(self):
        with self.lock:
            return list(self.traces)

    def get_errors(self):
        with self.lock:
            return list(self.errors)