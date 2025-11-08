from pydantic import BaseModel, ConfigDict
from typing import List

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    agents: List["Agent"] = []

    model_config = ConfigDict(from_attributes=True)
