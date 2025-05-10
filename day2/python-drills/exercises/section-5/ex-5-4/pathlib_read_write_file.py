from pathlib import Path


path = Path("sample.txt")
path.write_text("Hello, Python!")


content = path.read_text()
print("File content:", content)