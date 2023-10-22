from typing import Optional
from datetime import date

from pydantic import BaseModel, EmailStr, Field


class UserModel(BaseModel):
    name: str = Field('Andri', min_length=2, max_length=16)
    email: EmailStr
    password: str | None = Field(min_length=6, max_length=10)


class UserResponseSignupModel(BaseModel):
    name: str
    email: EmailStr
    detail: str | None = "User successfully created"


class UserResponse(BaseModel):
    id: int
    surname: str | None = Field('Andri', min_length=2, max_length=50)
    phone: str | None = Field('111111', min_length=10, max_length=14)
    detail: str | None = "User successfully created"

    class Config:
        from_attributes = True


class UserUpdateModel(BaseModel):
    name: Optional[str] = Field(None)
    email: Optional[EmailStr] = Field(None)
    surname: Optional[str] = Field(None)
    phone: Optional[str] = Field(None)


class UserUpdateResponse(BaseModel):
    id: int
    name: str
    surname: str | None
    email: EmailStr
    phone: str | None


class UserDeleteResponse(UserModel):
    password: None
    detail: str | None = "User successfully deleted"


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class ContactModel(BaseModel):
    name: Optional[str] = Field('Andri', min_length=2, max_length=150)
    surname: Optional[str] = Field('Andri', min_length=2, max_length=150)
    description: Optional[str] = Field(None)
    birthday: Optional[date] = Field(None)
    phone: Optional[str] = Field('111111', min_length=10, max_length=14)
    email: Optional[EmailStr]


class ContactResponse(ContactModel):
    id: int


class RequestEmail(BaseModel):
    email: EmailStr
