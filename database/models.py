from sqlmodel import SQLModel, Field


class UsersBase(SQLModel):
    user_id: int
    username: str
    telefon: str


class Users(UsersBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)


class UsersCreate(UsersBase):
    pass
