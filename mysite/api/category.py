from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List
from mysite.database.models import Category
from mysite.database.schema import CategoryInputSchema, CategoryOutSchema
from mysite.database.db import SessionLocal

category_router = APIRouter(prefix='/category', tags=['Category CRUD'])
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@category_router.post('/', response_model=CategoryOutSchema, status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryInputSchema, db: Session = Depends(get_db)):
    category_db = Category(**category.model_dump())
    db.add(category_db)
    db.commit()
    db.refresh(category_db)
    return category_db

@category_router.get('/', response_model=List[CategoryOutSchema])
def list_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()

@category_router.get('/{category_id}', response_model=CategoryOutSchema)
def detail_category(category_id: int, db: Session = Depends(get_db)):
    category_db = db.query(Category).filter(Category.id == category_id).first()
    if not category_db:
        raise HTTPException(status_code=404, detail='Category not found')
    return category_db

@category_router.put('/{category_id}/', response_model=dict)
async def update_category(category_id: int, category: CategoryInputSchema,
                          db: Session = Depends(get_db)):
    category_db = db.query(Category).filter(Category.id == category_id).first()
    if not category_db:
        raise HTTPException(detail='Мындай категория табылган жок', status_code=404)

    update_data = category.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(category_db, key, value)

    db.commit()
    db.refresh(category_db)
    return {'message': 'Категория ийгиликтүү өзгөртүлдү'}


@category_router.delete('/{category_id}/', response_model=dict)
async def delete_category(category_id: int, db: Session = Depends(get_db)):
    category_db = db.query(Category).filter(Category.id == category_id).first()
    if not category_db:
        raise HTTPException(detail='Мындай категория жок', status_code=404)

    db.delete(category_db)
    db.commit()
    return {'message': 'Категория удалить болду'}