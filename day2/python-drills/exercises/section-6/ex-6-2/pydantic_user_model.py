from pydantic import BaseModel, Field, conint, constr, ValidationError, validator
from typing import Optional

class Profile(BaseModel):
    bio: str

class User(BaseModel):
    name: constr(min_length=3)
    age: conint(gt=0)
    username: str
    profile: Optional[Profile] = None

    @validator("name")
    def name_must_be_capitalized(cls, v):
        if not v[0].isupper():
            raise ValueError("Name must start with a capital letter.")
        return v


try:
    u = User(name="Alice", age="42", username="alice123", profile={"bio": "Hello!"})
    print(u.dict())
    print(u.json())
except ValidationError as e:
    print(e)