from repositories.user_repository import UserRepository
from fastapi import HTTPException, status
from schemas.user_schema import CreateUserSchema
from core.secutiry import create_hash_password
class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo
    async def create_user(self, user_setting: CreateUserSchema):
        if await self.repo.get_user_by_username(user_setting.username) is not None:
            raise HTTPException(status_code= status.HTTP_409_CONFLICT, detailt ="username is busy")
        
        hashed = create_hash_password(user_setting.password)
        return await self.repo.create_user(
            username = user_setting.username,
            email = user_setting.email,
            password_hash = hashed
        )
        