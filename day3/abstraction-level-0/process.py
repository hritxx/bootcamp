import sys

for line in sys.stdin:
    stripped = line.strip()
    uppercased = stripped.upper()
    print(uppercased)