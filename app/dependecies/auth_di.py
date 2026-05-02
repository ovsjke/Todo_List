from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.repositories.auth_repository import AuthRepository
from app.services.auth_service import AuthService

async def get_auth_repo(session: AsyncSession = Depends(get_session)):
    return AuthRepository(session)

async def get_auth_service(repo: AuthRepository = Depends(get_auth_repo)):
    return AuthService(repo)