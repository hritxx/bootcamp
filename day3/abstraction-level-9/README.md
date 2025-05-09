# Real-Time File Processing System

## 🔧 Run Locally

```bash
# One-shot mode
python main.py --input somefile.txt

# Watch mode
python main.py --watch
```

## 🐳 Run with Docker

```bash
make build-docker
make run-docker
```

Mount `watch_dir/unprocessed` for real-time file watching.

## 🌐 FastAPI Endpoints

- `GET /health` – Health check endpoint for monitoring system status
- `GET /stats` – Retrieve statistics about processed files and system performance
- `POST /files` – Upload files for processing via HTTP

## 📤 Upload Files

```bash
curl -F 'file=@yourfile.txt' http://localhost:8000/files
```

Or use `rsync`:

```bash
rsync yourfile.txt user@host:/path/to/watch_dir/unprocessed/
```

## 📊 Uptime Monitoring

Use [Better Uptime](https://betteruptime.com/) to monitor the health endpoint:

```
http://hriteekroy1869.chickenkiller.com:8000/health
```

## 🚀 Cloud Deployment

This system is currently deployed on an Azure VM at:

```
http://hriteekroy1869.chickenkiller.com:8000/health
```

Access the health endpoint at: http://hriteekroy1869.chickenkiller.com:8000/health

## 📋 Available Make Commands

```
make build-docker    # Build the Docker image
make run-docker      # Run the container with proper volume mounts
make clean           # Remove temporary files and build artifacts
make build-package   # Build the Python package
make publish-package # Publish the package to PyPI
```

## ✅ Features

- Dual execution modes (single file / watch)
- Docker-ready deployment
- Upload via browser, curl, or file sync
- Comprehensive FastAPI server with statistics
- Azure cloud deployment
- Makefile for automation and simplified operations
