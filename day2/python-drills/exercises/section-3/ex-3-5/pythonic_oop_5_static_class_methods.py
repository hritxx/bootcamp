class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @staticmethod
    def is_valid_isbn(isbn):
        return isbn.isdigit() and len(isbn) in (10, 13)

    @classmethod
    def from_string(cls, s):
        title, author = s.split("|")
        return cls(title.strip(), author.strip())

    def describe(self):
        return f"{self.title} by {self.author}"


class Novel(Book):
    @classmethod
    def from_string(cls, s):
        title, author = s.split("|")
        return cls(title.strip(), author.strip())


print(Book.is_valid_isbn("1234567890"))
book = Book.from_string("1984 | Orwell")
print(book.describe())

novel = Novel.from_string("Dune | Herbert")
print(isinstance(novel, Novel))