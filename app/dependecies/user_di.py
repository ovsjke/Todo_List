from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.repositories.user_repository import UserRepository
from app.services.user_serviece import UserService

async def get_user_repo(session: AsyncSession = Depends(get_session)):
    return UserRepository(session)

async def get_user_service(repo: UserRepository = Depends(get_user_repo)):
    return UserService(repo)