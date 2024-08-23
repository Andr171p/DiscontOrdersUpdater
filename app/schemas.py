from pydantic import BaseModel


class UserSchema(BaseModel):
    user_id: int
    username: str
    telefon: str
