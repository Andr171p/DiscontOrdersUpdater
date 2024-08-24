from fastapi import FastAPI

import contextlib

from typing import AsyncIterator

from database.manage import init_models

from app.api import router


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    await init_models()
    yield


app = FastAPI(title="Registration in database API", lifespan=lifespan)
app.include_router(router, prefix="/api/registration", tags=["registration"])
