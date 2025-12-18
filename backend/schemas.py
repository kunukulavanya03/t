from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class UsersBase(BaseModel):
    name: str
    description: Optional[str] = None

class UsersCreate(UsersBase):
    pass

class UsersResponse(UsersBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class ProductsBase(BaseModel):
    name: str
    description: Optional[str] = None

class ProductsCreate(ProductsBase):
    pass

class ProductsResponse(ProductsBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class OrdersBase(BaseModel):
    name: str
    description: Optional[str] = None

class OrdersCreate(OrdersBase):
    pass

class OrdersResponse(OrdersBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class PaymentsBase(BaseModel):
    name: str
    description: Optional[str] = None

class PaymentsCreate(PaymentsBase):
    pass

class PaymentsResponse(PaymentsBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class DataBase(BaseModel):
    name: str
    description: Optional[str] = None

class DataCreate(DataBase):
    pass

class DataResponse(DataBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class DatabaseBase(BaseModel):
    name: str
    description: Optional[str] = None

class DatabaseCreate(DatabaseBase):
    pass

class DatabaseResponse(DatabaseBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class CreateBase(BaseModel):
    name: str
    description: Optional[str] = None

class CreateCreate(CreateBase):
    pass

class CreateResponse(CreateBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

