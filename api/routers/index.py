from fastapi import APIRouter

from api.controllers import users, todo

router = APIRouter()

router.include_router(users.router)
router.include_router(todo.router)