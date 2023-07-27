from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str
    password: str

class UserRequest(UserBase):
    ...

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True

class AuthenticateBase(BaseModel):
    email: str
    password: str

class AuthenticateRequest(AuthenticateBase):
    ...