from fastapi import APIRouter, Depends, status

from app.schemas.user_schema import CreateUserSchema, ReturnUserSchema
from app.services.user_serviece import UserService
from app.dependecies.user_di import get_user_service
from app.core.securities.security_di import get_current_user
from app.core.models import User

router = APIRouter(prefix="/users", tags = ["Users"])

@router.post("/signup", response_model= ReturnUserSchema, summary = "Sign up user", status_code= status.HTTP_201_CREATED)
async def create_user(
    data: CreateUserSchema,
    service: UserService = Depends(get_user_service)):
    new_user = await service.create_user(data)
    return new_user


@router.get("/profile", response_model= ReturnUserSchema, summary="User profile")
async def user_profile(
    current_user: User = Depends(get_current_user)
):
    return current_user