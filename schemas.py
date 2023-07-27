from pydantic import BaseModel

class UserBase(BaseModel):
    nome: str
    email: str
    senha: str

class UserRequest(UserBase):
    ...

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True

class AuthenticateBase(BaseModel):
    email: str
    senha: str

class AuthenticateRequest(AuthenticateBase):
    ...