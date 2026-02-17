from pydantic import BaseModel, EmailStr
from typing import Optional
from .models import StatusChoices
from datetime import date,datetime


class UserProfileInputSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    password: str
    age: Optional[int]
    phone_number: Optional[str]


class UserProfileOutSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    age: Optional[int]
    phone_number: Optional[str]
    status: StatusChoices
    date_register:date

class CategoryInputSchema(BaseModel):
    category_name: str
    category_image: str

class CategoryOutSchema(BaseModel):
    id: int
    category_name: str
    category_image: str

class SubCategoryInputSchema(BaseModel):
    sub_category_name: str
    category_id: int

class SubCategoryOutSchema(BaseModel):
    id: int
    sub_category_name: str
    category_id: int

class ProductInputSchema(BaseModel):
    subcategory_id: int
    product_name: str
    price: int
    article_number: int
    description: str
    video: Optional[str]
    product_type: bool


class ProductOutSchema(BaseModel):
    id: int
    subcategory_id: int
    product_name: str
    price: int
    article_number: int
    description: str
    video: Optional[str]
    product_type: bool
    created_date: date


class ProductImageInputSchema(BaseModel):
    image: str
    product_id: int

class ProductImageOutSchema(BaseModel):
    id: int
    image: str
    product_id: int

class ReviewInputSchema(BaseModel):
    user_id: int
    product_id: int
    text: str
    stars: int

class ReviewOutSchema(BaseModel):
    id: int
    user_id: int
    product_id: int
    text: str
    stars: int
    created_date: datetime

class UserLoginSchema(BaseModel):
    username: str
    password: str