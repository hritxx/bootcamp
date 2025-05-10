from collections import defaultdict

words = ["apple", "banana", "apricot", "blueberry", "cherry"]
grouped = defaultdict(list)

for word in words:
    grouped[word[0]].append(word)

for key, value in grouped.items():
    print(f"{key}: {value}")