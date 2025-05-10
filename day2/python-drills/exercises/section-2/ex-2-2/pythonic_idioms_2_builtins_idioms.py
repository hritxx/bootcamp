
fruits = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(fruits):
    print(i, fruit)


a = [1, 2, 3]
b = ['a', 'b', 'c']
for pair in zip(a, b):
    print(pair)


nums = [1, -2, 3]
print("Any negative?", any(n < 0 for n in nums))
print("All positive?", all(n > 0 for n in nums))
pairs = [(2, 3), (1, 2), (3, 1)]
print(sorted(pairs, key=lambda x: x[1]))

nums = [1, 2, 3, 4]
print(list(map(lambda x: x * 2, nums)))
print(list(filter(lambda x: x % 2, nums)))


x = 5
if 0 < x < 10:
    print("x is in range")


x, y = 1, 2
x, y = y, x
print(x, y)


for x, y in [(1, 2), (3, 4)]:
    print(x, y)
