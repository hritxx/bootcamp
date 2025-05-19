import argparse
from app.processor import process_file
from app.watcher import watch_directory

def main():
    parser = argparse.ArgumentParser(description="Real-Time File Processor")
    parser.add_argument("--input", help="Single file to process")
    parser.add_argument("--watch", action="store_true", help="Watch directory for files")

    args = parser.parse_args()

    if args.input:
        process_file(args.input)
    elif args.watch:
        watch_directory()
    else:
        print("Provide either --input <file> or --watch")

if __name__ == "__main__":
    main()
