import json

class User:
    def __init__(self, username, password):
        self.username = username
        self._password = password  

    def to_safe_dict(self):
        return {"username": self.username}

    def to_json(self):
        return json.dumps(self.to_safe_dict())

user = User("john", "secret123")
print(user.to_json())