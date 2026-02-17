from fastapi import APIRouter, HTTPException, Depends
from mysite.database.models import UserProfile
from mysite.database.schema import UserProfileInputSchema,UserProfileOutSchema
from mysite.database.db import SessionLocal
from sqlalchemy.orm import Session
from typing import List


user_router = APIRouter(prefix='/user', tags=['UserProfile'])
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@user_router.post('/', response_model=UserProfileOutSchema)
async def create_user(user:UserProfileInputSchema, db:Session = Depends(get_db)):
    user_db = UserProfile(**user.dict())
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db

@user_router.get('/', response_model=List[UserProfileOutSchema])
async def list_user(db:Session = Depends(get_db)):
    return  db.query(UserProfile).all()

@user_router.get('/{user_id}', response_model=UserProfileOutSchema)
async def detail_user(user_id:int, db:Session = Depends(get_db)):
    user_db = db.query(UserProfile).filter(UserProfile.id == user_id).one_or_none()
    if not user_db:
        raise HTTPException(detail='User not found',status_code=404,)
    return user_db



@user_router.put('/{user_id}/', response_model=dict)
async def update_user(user_id: int, user: UserProfileInputSchema,
                     db: Session = Depends(get_db)):
    user_db = db.query(UserProfile).filter(UserProfile.id == user_id).first()
    if not user_db:
        raise HTTPException(detail='Мындай колдонуучу табылган жок', status_code=404)


    update_data = user.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(user_db, key, value)

    db.commit()
    db.refresh(user_db)
    return {'message': 'Колдонуучу ийгиликтүү өзгөртүлдү'}


@user_router.delete('/{user_id}/', response_model=dict)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_db = db.query(UserProfile).filter(UserProfile.id == user_id).first()
    if not user_db:
        raise HTTPException(detail='Мындай колдонуучу жок', status_code=404)


    db.delete(user_db)
    db.commit()
    return {'message': 'Колдонуучу өчүрүлдү'}