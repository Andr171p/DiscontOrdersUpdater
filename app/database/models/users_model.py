from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy import BigInteger


class Base(DeclarativeBase):
    pass


class AbstractModel(AsyncAttrs, Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True
    )


class UsersModel(AbstractModel):
    user_id: Mapped[int] = mapped_column(BigInteger)
    username: Mapped[str] = mapped_column()
    telefon: Mapped[str] = mapped_column()
