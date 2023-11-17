
from fastapi import APIRouter
from api.dto.user import User

users = [] # In memory storage


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)



@router.post("/")
async def create_user(user: User):
    users.append(user)
    return user


@router.get("/")
async def get_users():
    return users


@router.get("/{user_id}")
async def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return {"message": "User not found"}

@router.put("/{user_id}")
async def update_user(user_id: int, user: User):
    for _user in users:
        if _user.id == user_id:
            _user.name = user.name
            _user.email = user.email
            _user.password = user.password
            return _user
    return {"message": "User not found"}

@router.delete("/{user_id}")
async def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return {"message": "User deleted"}
    return {"message": "User not found"}




   



