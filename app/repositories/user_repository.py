from sqlalchemy.ext.asyncio import AsyncSession
from app.core.models import User
from app.schemas.user_schema import CreateUserDBSchema
from sqlalchemy import select

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
    async def create_user(self, user_setting: CreateUserDBSchema) -> User:
        password = user_setting.password_hash
        new_user = User(
            username = user_setting.username,
            email = user_setting.email,
            password_hash = password
        )
        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)

        return new_user
    async def get_user_by_username(self, username: str) -> User:
        stmt = select(User).where(User.username == username)
        result = await self.session.execute(stmt)
        user = result.scalar_one_or_none()
        return user