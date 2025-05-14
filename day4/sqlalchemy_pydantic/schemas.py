from pydantic import BaseModel, EmailStr, validator, Field
from typing import List, Optional, Annotated
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: Annotated[str, Field(min_length=8)]

class UserSchema(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class PostSchema(PostBase):
    id: int
    user_id: int
    created_at: datetime
    
    class Config:
        orm_mode = True

class UserWithPosts(UserSchema):
    posts: List[PostSchema] = []
    
    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    description: str
    price: float

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None

class ProductSchema(ProductBase):
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True

class UserEmailHistorySchema(BaseModel):
    id: int
    user_id: int
    email: EmailStr
    changed_at: datetime
    
    class Config:
        orm_mode = True

class AccountSchema(BaseModel):
    id: int
    user_id: int
    balance: float
    
    class Config:
        orm_mode = True

class TransferSchema(BaseModel):
    from_account_id: int
    to_account_id: int
    amount: float = Field(..., gt=0)

class ProfileImageSchema(BaseModel):
    id: int
    user_id: int
    image_path: str
    uploaded_at: datetime
    
    class Config:
        orm_mode = True
