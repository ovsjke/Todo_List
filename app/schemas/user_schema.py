from pydantic import BaseModel, Field, EmailStr, model_validator, ConfigDict
from datetime import datetime
from fastapi import HTTPException, status

class CreateUserSchema(BaseModel):
    username: str = Field(...,min_length = 3, max_length = 30, description= "Имя пользователя")
    email: EmailStr = Field(...,  description="Почта")
    password: str = Field(..., min_length = 4, description= "Пароль")
    @model_validator(mode = "after")
    def validate_password(self):
        if self.username == self.password:
            raise HTTPException(status.HTTP_422_UNPROCESSABLE_CONTENT, detail = "password must differ from username")
        return self

class ReturnUserSchema(BaseModel):
    model_config = ConfigDict(from_attributes= True)
    username: str
    email: str
    created_at: datetime

class CreateUserDBSchema(BaseModel):
    username:str
    email: EmailStr
    password_hash: str