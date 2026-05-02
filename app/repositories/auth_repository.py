from sqlalchemy.ext.asyncio import AsyncSession
from app.core.models import User
from app.schemas.auth_schema import AuthUserSchema
from sqlalchemy import select

class AuthRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
    async def get_user_by_username_or_email(self, user_data: AuthUserSchema):
        stmt = select(User).where((User.username == user_data.login) | (User.email == user_data.login))
        result = await self.session.execute(stmt)
        user = result.scalar_one_or_none()
        return user
