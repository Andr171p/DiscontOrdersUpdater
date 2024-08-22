from app.root import app

from database.models import Users, UsersCreate
from database.engine import init_db, get_session
from database import manage

from fastapi import Depends

from sqlmodel.ext.asyncio.session import AsyncSession


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/users", response_model=list[Users])
async def get_users(session: AsyncSession = Depends(get_session)):
    users = await manage.db_get_users(session=session)
    return users


@app.post("/users")
async def add_user(user: UsersCreate, session: AsyncSession = Depends(get_session)):
    user = await manage.db_add_user(user=user, session=session)
    return user