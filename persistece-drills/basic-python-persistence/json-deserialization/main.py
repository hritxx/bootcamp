import json

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(**data)

json_str = '{"title": "1984", "author": "George Orwell"}'
book = Book.from_json(json_str)
print(book.__dict__)