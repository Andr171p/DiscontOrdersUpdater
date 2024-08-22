from fastapi import Depends

from sqlmodel import select

from sqlmodel.ext.asyncio.session import AsyncSession

from database.engine import init_db, get_session
from database.models import Users, UsersCreate


async def db_get_users(session: AsyncSession = Depends(get_session)):
    data = await session.execute(select(Users))
    users = data.scalars().all()
    result = [
        Users(
            user_id=user.user_id,
            username=user.username,
            telefon=user.telefon
        ) for user in users
    ]
    return result


async def db_add_user(user: UsersCreate, session: AsyncSession = Depends(get_session)):
    user = Users(
        user_id=user.user_id,
        username=user.username,
        telefon=user.telefon
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
