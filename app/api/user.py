from fastapi import APIRouter, Depends

from schemas.user_schema import CreateUserSchema, ReturnUserSchema
from services.user_serviece import UserService
from dependecies.user_dependecies import get_user_service

router = APIRouter(prefix="/users", tags = ["Users"])

@router.post("/signup", response_model= ReturnUserSchema)
async def create_user(
    data: CreateUserSchema,
    service: UserService = Depends(get_user_service)):
    new_user = await service.create_user(data)
    return new_user