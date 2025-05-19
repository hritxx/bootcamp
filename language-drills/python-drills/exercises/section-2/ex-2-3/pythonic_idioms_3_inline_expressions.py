
x = 5
print("Even" if x % 2 == 0 else "Odd")

a = b = 10
print(a, b)


flag = True
print("Yes" if flag else "No")


a, b, *rest = [1, 2, 3, 4, 5]
print(a, b, rest)

name = "" or "Anonymous"
print(name)


is_admin = True
is_admin and print("Delete user")


labels = ['even' if x % 2 == 0 else 'odd' for x in range(5)]
print(labels)
