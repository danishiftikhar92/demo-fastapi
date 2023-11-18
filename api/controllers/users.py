
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from api.dto.user import User, UserCreate
from api.models.users import Users
from api.config.db import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)



@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    user = Users(name=payload.name, email=payload.email, password=payload.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User created successfully", "data": user}


@router.get("/")
async def get_users(db: Session = Depends(get_db), skip: int = 0, page: int = 1, limit: int = 100, search: str = ""):
    skip = (page - 1) * limit
    users = db.query(Users).filter(Users.name.like(f"%{search}%")).offset(skip).limit(limit).all()
    return {"message": "Users retrieved successfully", "data": users}


@router.get("/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(Users).filter(Users.id == user_id).first()
    if user:
        return {"message": "User retrieved successfully", "data": user}
    return {"message": "User not found"}
    

@router.put("/{user_id}")
async def update_user(user_id: int, user: User, db: Session = Depends(get_db)):
   user = db.query(Users).filter(Users.id == user_id).first()
   if user:
         user.name = user.name
         user.email = user.email
         user.password = user.password
         db.commit()
         db.refresh(user)
         return {"message": "User updated successfully", "data": user}
   return {"message": "User not found"}


@router.delete("/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(Users).filter(Users.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return {"message": "User deleted successfully"}
    return {"message": "User not found"}




   



