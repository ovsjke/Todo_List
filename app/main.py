import asyncio
from fastapi import FastAPI
import uvicorn
from app.core.database import Base
from app.core.database import engine




def create_app() -> FastAPI:
    app = FastAPI()



    return app

app = create_app

async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

def run_api() -> None:
    uvicorn.run(app, host = "0.0.0.0", port = 8000, reload= False)

if __name__ == "__main__":
    asyncio.run(init_db())
    run_api()