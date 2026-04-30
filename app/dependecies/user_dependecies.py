from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_session
from repositories.user_repository import UserRepository
from services.user_serviece import UserService

async def get_user_repo(session: AsyncSession = Depends(get_session)):
    return UserRepository(session)

async def get_user_service(repo: UserRepository = Depends(get_user_repo)):
    return UserService(repo)