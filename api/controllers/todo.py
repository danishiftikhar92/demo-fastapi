from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from api.config.db import get_db
from api.dto.todo import  TodoCreate, TodoUpdate
from api.models.todo import TodoList

router = APIRouter(
    prefix="/todo",
    tags=["todo"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_todo(payload: TodoCreate, db: Session = Depends(get_db)):
   todo = TodoList(title=payload.title, description=payload.description, owner_id=payload.owner_id)
   db.add(todo)
   db.commit()
   db.refresh(todo)
   return {"message": "Todo created successfully", "data": todo}


@router.get("/")
async def get_todos(db: Session = Depends(get_db), skip: int = 0, page: int = 1, limit: int = 100, search: str = ""):
    skip = (page - 1) * limit
    todos = db.query(TodoList).filter(TodoList.title.like(f"%{search}%")).offset(skip).limit(limit).all()
    return {"message": "Todos retrieved successfully", "data": todos}


@router.get("/{todo_id}")
async def get_todo_by_id(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoList).filter(TodoList.id == todo_id).first()
    if todo:
        return {"message": "Todo retrieved successfully", "data": todo}
    return {"message": "Todo not found"}

@router.put("/{todo_id}")
async def update_todo_by_id(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    todo = db.query(TodoList).filter(TodoList.id == todo_id).first()
    if todo:
        todo.title = todo.title
        todo.description = todo.description
        todo.owner_id = todo.owner_id
        todo.status = todo.status
        db.commit()
        db.refresh(todo)
        return {"message": "Todo updated successfully", "data": todo}
    return {"message": "Todo not found"}

@router.delete("/{todo_id}")
async def delete_todo_by_id(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoList).filter(TodoList.id == todo_id).first()
    if todo:
        db.delete(todo)
        db.commit()
        return {"message": "Todo deleted successfully"}
    return {"message": "Todo not found"}