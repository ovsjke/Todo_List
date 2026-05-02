from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.auth_schema import AuthUserSchema
from app.services.auth_service import AuthService
from app.dependecies.auth_di import get_auth_service

router = APIRouter(prefix = "/auth", tags = ["auth"])

@router.post("/login", summary= "auth",)
async def auth_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: AuthService = Depends(get_auth_service)
):
    data = AuthUserSchema(login = form_data.username, password = form_data.password)
    return await service.pass_verification(data)