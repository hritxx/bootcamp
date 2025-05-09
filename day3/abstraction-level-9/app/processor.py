import os

def process_file(filepath):
    print(f"[+] Processing file: {filepath}")
    # Your actual processing logic here
    with open(filepath, 'r') as f:
        content = f.read()
        print(content)
