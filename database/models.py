from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer

from database.base import base


class Users(base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    user_id = Column(Integer, unique=True)
    username = Column(String)
    telefon = Column(String)
