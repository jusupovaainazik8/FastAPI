from mysite.database.models import *
from sqladmin import ModelView


class UserProfileAdmin(ModelView, model=UserProfile):
    column_list = [UserProfile.first_name, UserProfile.last_name]


class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.id, Category.category_name]

class ProductAdmin(ModelView, model=Product):
    column_list = [Product.product_name]

class ProductImageAdmin(ModelView, model=ProductImage):
    column_list = [ProductImage.product_id, ProductImage.image]

class SubCategoryAdmin(ModelView, model=SubCategory):
    column_list = [SubCategory.sub_category_name]

class ReviewAdmin(ModelView, model=Review):
    column_list = [Review.id, Review.stars]