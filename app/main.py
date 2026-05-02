from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

from app.core.database import Base, engine
from app.api import user, auth
import app.core.models  # noqa: F401


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.include_router(user.router)
    app.include_router(auth.router)
    return app


if __name__ == "__main__":
    uvicorn.run(create_app(), host="0.0.0.0", port=8000, reload=False)
