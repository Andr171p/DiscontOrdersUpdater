from pydantic import BaseModel, ConfigDict, Field

from typing import Literal, List


class UserResponse(BaseModel):
    id: int
    user_id: int
    username: str
    telefon: str

    model_config = ConfigDict(from_attributes=True)


class UsersResponse(BaseModel):
    data: List[UserResponse]


class APIUserResponse(BaseModel):
    status: Literal["ok"] = "ok"
    data: UserResponse


class APIUserListResponse(BaseModel):
    status: Literal["ok"] = "ok"
    data: list[UserResponse]


class AddUserRequest(BaseModel):
    user_id: int
    username: str
    telefon: str
