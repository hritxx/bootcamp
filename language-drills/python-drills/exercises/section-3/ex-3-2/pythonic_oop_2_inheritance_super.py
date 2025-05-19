class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        return f"{self.title} by {self.author}"

    def __str__(self):
        return self.describe()


class Novel(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

    def describe(self):
        return "Novel: " + super().describe()


class AudioMixin:
    def play_audio(self):
        return f"Playing audio for {self.title}"


class AudioBook(AudioMixin, Book):
    pass


books = [Book("1984", "Orwell"), Novel("Dune", "Herbert", "Sci-Fi")]
for b in books:
    print(b.describe())

print(isinstance(books[1], Book))