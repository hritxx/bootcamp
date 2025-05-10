class Book:
    category = "Fiction"

    def __init__(self, title="Untitled", author="Unknown"):
        self.title = title
        self.author = author

    def describe(self):
        return f"{self.title} by {self.author}"

    def update_title(self, new_title):
        self.title = new_title


book = Book("1984", "Orwell")
print(book.describe())


print(book.category)


book.update_title("Animal Farm")
print(book.describe())


book.year = 1945
print(book.year)


print(isinstance(book, Book))