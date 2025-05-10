# List Comprehension with Condition
print([x**2 for x in [1, 2, 3, 4] if x % 2 == 0])  # [4, 16]

# Nested List Comprehension
print([x for sub in [[1, 2], [3, 4]] for x in sub])  # [1, 2, 3, 4]

# Dict Comprehension
print({k: 1 for k in ["a", "b"]})  # {'a': 1, 'b': 1}

# Set Comprehension
print({ch for ch in "hello world" if ch in "aeiou"})  # {'e', 'o'}

# Generator Expression
gen = (n*n for n in range(5))
print(list(gen))  # [0, 1, 4, 9, 16]


# Filter with Comprehension
print([s for s in ["hi", "hello", "bye"] if len(s) % 2 == 0])  # ['hi']

# Conditional Assignment
nums = [1, -2, 3, -4]
print([x if x >= 0 else 0 for x in nums])  # [1, 0, 3, 0]