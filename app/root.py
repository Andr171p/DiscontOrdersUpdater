import contextlib
from typing import AsyncIterator

import uvicorn
from fastapi import FastAPI

from database.manage import init_models

from app.api import router


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    await init_models()
    yield
    await orm.db_manager.close()


app = FastAPI(title="Registration in database API", lifespan=lifespan)
app.include_router(router, prefix="/api/registration", tags=["registration"])
