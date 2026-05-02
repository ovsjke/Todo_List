from app.repositories.user_repository import UserRepository
from fastapi import HTTPException, status
from app.schemas.user_schema import CreateUserSchema
from app.core.securities.secutiry  import create_hash_password
from uuid import UUID

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo
    async def create_user(self, user_setting: CreateUserSchema):
        if await self.repo.get_user_by_username(user_setting.username) is not None:
            raise HTTPException(status_code= status.HTTP_409_CONFLICT, detail ="username is busy")
        
        hashed = create_hash_password(user_setting.password)
        user_data = CreateUserDBSchema(
        username=user_setting.username,
        email=user_setting.email,
        password_hash=hashed,
    )
        return await self.repo.create_user(
            user_data
        )
    async def get_user_by_id(self, user_id: UUID):
        return await self.repo.get_user_by_id(user_id)