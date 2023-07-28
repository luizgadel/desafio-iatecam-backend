from pydantic import BaseModel

'''
USER
'''
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

'''
AUTHENTICATE
'''
class AuthenticateBase(BaseModel):
    email: str
    password: str

class AuthenticateRequest(AuthenticateBase):
    ...

'''
CATEGORY
'''
class CategoryBase(BaseModel):
    description: str

class CategoryRequest(CategoryBase):
    ...

class CategoryResponse(CategoryBase):
    id: int
    
    class Config:
        from_attributes = True

'''
PRODUCT
'''
class ProductBase(BaseModel):
    description: str
    value: int
    category_id: int
    quantity: int
    
class ProductRequest(ProductBase):
    ...

class ProductResponse(ProductBase):
    id: int
    
    class Config:
        from_attributes = True