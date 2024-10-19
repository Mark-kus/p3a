from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.user import UserModel
from database import get_db
from schemas.user import User, UserCreate

user_router = APIRouter()


@user_router.get("/")
async def get_users(db: Session = Depends(get_db)):
    return UserModel().get_all(db)


@user_router.get("/filter")
async def get_user_by_filter(name: str, db: Session = Depends(get_db)):
    return UserModel().get_by_filter(db, name=name)


@user_router.get("/filter_first")
async def get_user_by_filter_first(name: str, db: Session = Depends(get_db)):
    return UserModel().get_by_filter_first(db, name=name)


@user_router.get("/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    return UserModel().get_by_id(db, user_id)


@user_router.post("/")
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserModel().create(db, UserModel(**user.model_dump()))


@user_router.put("/{user_id}")
async def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    exists = UserModel().get_by_id(db, user_id)
    if not exists:
        raise HTTPException(status_code=404, detail="User not found")

    return UserModel().update(db, user_id, UserModel(**user.model_dump()))


@user_router.delete("/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    exists = UserModel().get_by_id(db, user_id)
    if not exists:
        raise HTTPException(status_code=404, detail="User not found")

    return UserModel().delete(db, user_id)
