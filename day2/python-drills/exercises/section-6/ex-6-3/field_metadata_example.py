from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(..., alias="user_id", description="Unique user identifier", example=101)
    email: str = Field(..., description="User's email address", title="Email")

print(User.schema_json(indent=2))