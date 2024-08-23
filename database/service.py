from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Users


async def get_all_users(session: AsyncSession) -> list[Users]:
    users = await session.execute(select(Users))
    return users.scalars().all()


def add_user(session: AsyncSession, user_id: int, username: str, telefon: str):
    new_user = Users(
        user_id=user_id,
        username=username,
        telefon=telefon
    )
    session.add(new_user)
    return new_user
