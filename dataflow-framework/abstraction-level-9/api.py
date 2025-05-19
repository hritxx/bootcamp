from fastapi import FastAPI, UploadFile, File
from app.processor import process_file
import os

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/stats")
def stats():
    return {"processed_files": len(os.listdir("watch_dir/processed"))}

@app.post("/files")
async def upload(file: UploadFile = File(...)):
    path = f"watch_dir/unprocessed/{file.filename}"
    with open(path, "wb") as f:
        content = await file.read()
        f.write(content)
    return {"filename": file.filename}
