import asyncio
from fastapi import FastAPI
import uvicorn
from  core.database import Base, engine
from api import user
import app.core.models  # noqa: F401




def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(user.router)
    return app


async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

def run_api() -> None:
    uvicorn.run(create_app(), host = "0.0.0.0", port = 8000, reload= False)

if __name__ == "__main__":
    asyncio.run(init_db())
    run_api()