from sqlalchemy import Column, Integer, String

from models.base import model_methods
from database import Base


@model_methods
class UserModel(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
