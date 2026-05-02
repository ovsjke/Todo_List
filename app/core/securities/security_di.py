from fastapi import status, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, HTTPBearer, HTTPAuthorizationCredentials
from app.services.user_serviece import UserService
from app.dependecies.user_di import get_user_service
from app.core.securities.secutity import jwt_decode
from uuid import UUID

security = HTTPBearer()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl= "auth/login")

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    user_service: UserService = Depends(get_user_service),
):
    token = credentials.credentials

    payload = jwt_decode(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    user = await user_service.get_user_by_id(UUID(user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return user   

