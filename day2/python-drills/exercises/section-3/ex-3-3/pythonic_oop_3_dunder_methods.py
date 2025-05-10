class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title}"
    
    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r})"

    def __eq__(self, other):
        return (self.title, self.author) == (other.title, other.author)

    def __hash__(self):
        return hash((self.title, self.author))

    def __lt__(self, other):
        return self.title < other.title


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __len__(self):
        return len(self.books)

    def __getitem__(self, index):
        return self.books[index]


class Greeter:
    def __call__(self, name):
        return f"Hello, {name}!"


class AlwaysFalse:
    def __bool__(self):
        return False


b1 = Book("1984", "Orwell")
b2 = Book("1984", "Orwell")
print(b1 == b2)
print(set([b1, b2]))

lib = Library()
lib.add_book(b1)
print(len(lib), lib[0])

greet = Greeter()
print(greet("Alice"))

af = AlwaysFalse()
print(bool(af))