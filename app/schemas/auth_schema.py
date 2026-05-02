from pydantic import BaseModel, EmailStr, Field

class AuthUserSchema(BaseModel):
    login: EmailStr | str = Field(description= "Логин или почта")
    password: str