from sqlmodel import SQLModel, Field
from datetime import datetime


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str
    created_time: datetime = Field(default=datetime.now())

class Books(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    author: str
    year: int