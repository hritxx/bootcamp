# List Operations
a = [5, 3, 8]
a.append(2)
a.remove(3)
a.sort()
print(a)  # [2, 5, 8]

# List Slicing
lst = [1, 2, 3, 4, 5, 6, 7]
print(lst[2:5])  # [3, 4, 5]

# List Copying Pitfall
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4]
a = [1, 2, 3]
b = a[:]
b.append(4)
print(a)  # [1, 2, 3]

# Dictionary Access
user = {"name": "Alice"}
print(user.get("age", "N/A"))  # N/A
user.setdefault("age", 25)
print(user)  # {'name': 'Alice', 'age': 25}

# Dictionary Iteration
person = {"name": "Bob", "age": 30}
for k, v in person.items():
    print(k, v)


a = {1, 2, 3}
b = {3, 4}
print(a & b)  
print(a | b) 
print(a - b)  


x, y, z = (7, 8, 9)
print(x, y, z)


t = (1, 2, 3)
try:
    t[0] = 100
except TypeError as e:
    print(e)  # 'tuple' object does not support item assignment