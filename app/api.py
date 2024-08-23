from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from app.models import AddUserRequest
from app.models import UserResponse, UsersResponse
from app.models import APIUserResponse, APIUserListResponse

from app.exeptions import DuplicatedEntryError

from database.manage import get_session
from database import service

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession


'''@app.get("/users/all", response_model=list[UserSchema])
async def get_all_users(session: AsyncSession = Depends(get_session)):
    users = await service.get_all_users(session=session)
    result = [
        UserSchema(
            user_id=user.user_id,
            username=user.username,
            telefon=user.telefon
        ) for user in users
    ]
    return result


@app.post("/users/")
async def add_user(user: UserSchema, session: AsyncSession = Depends(get_session)):
    user = service.add_user(
        session=session,
        user_id=user.user_id,
        username=user.username,
        telefon=user.telefon
    )
    try:
        await session.commit()
        return user
    except IntegrityError as _ex:
        await session.rollback()
        raise DuplicatedEntryError(message="The user is already stored")'''


router = APIRouter()


@router.get("/all_users/", response_model=APIUserListResponse)
async def get_all_users(
        session: AsyncSession = Depends(get_session)
) -> JSONResponse:
    users = await service.get_all_users(session=session)
    if not users:
        return JSONResponse(
            content={"status": "error", "message": "Users not found"},
            status_code=status.HTTP_404_NOT_FOUND,
        )
    response_model = UsersResponse.model_validate(users)
    return JSONResponse(
        content={
            "status": "ok",
            "data": response_model.model_dump(),
        }
    )


@router.post("/add_user/", response_model=APIUserResponse, status_code=status.HTTP_201_CREATED)
async def add_user(
        user: AddUserRequest, session: AsyncSession = Depends(get_session)
) -> JSONResponse:
    user = service.add_user(
        session=session,
        user_id=user.user_id,
        username=user.username,
        telefon=user.telefon
    )
    try:
        await session.commit()
        await session.refresh(user)
        response_model = UserResponse.model_validate(user)
        return JSONResponse(
            content={
                "status": "ok",
                "data": response_model.model_dump(),
            },
            status_code=status.HTTP_201_CREATED,
        )
    except IntegrityError as _ex:
        await session.rollback()
        raise DuplicatedEntryError(message="The user is already stored")