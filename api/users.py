from typing import List, Optional

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from api.utils.users import create_user, get_user, get_user_by_email, get_users
from db.db_setup import get_db
from pydantic_schemas.user import User, UserCreate

router = fastapi.APIRouter()


@router.get("/users", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.post("/users")
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)


@router.get("/users/{user_id}")
async def read_user(user_id: int, db: Session = Depends(get_db)):
    return get_user(db=db, user_id=user_id)
