from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class User(UserCreate):
    user_id: int

    class Config:
        from_attributes = True
