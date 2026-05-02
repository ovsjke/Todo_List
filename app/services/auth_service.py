from app.repositories.auth_repository import AuthRepository
from fastapi import HTTPException, status
from app.schemas.auth_schema import AuthUserSchema
from app.core.secutity import check_password, jwt_encode

class AuthService:
    def __init__(self, repo: AuthRepository):
        self.repo = repo
    async def pass_verification(self, data: AuthUserSchema):
        user = await self.repo.get_user_by_username_or_email(data)
        if (user is not None) and check_password(user.password_hash, data.password):
            access_token = jwt_encode(id = user.id)
            return {"access_token": access_token, "token_type": "bearer"}
        else:
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail = "Incorrect password or login")
        