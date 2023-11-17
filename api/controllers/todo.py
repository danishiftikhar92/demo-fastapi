from fastapi import APIRouter
from api.dto.todo import Todo


todoList = [] # In memory storage

router = APIRouter(
    prefix="/todo",
    tags=["todo"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def create_todo(todo: Todo):
    todoList.append(todo)
    return todo


@router.get("/")
async def get_todos():
    return todoList


@router.get("/{todo_id}")
async def get_todo_by_id(todo_id: int):
    for todo in todoList:
        if todo.id == todo_id:
            return todo
    return {"message": "Todo not found"}

@router.put("/{todo_id}")
async def update_todo_by_id(todo_id: int, todo: Todo):
    for _todo in todoList:
        if _todo.id == todo_id:
            _todo.title = todo.title
            _todo.description = todo.description
            _todo.owner_id = todo.owner_id
            return _todo
    return {"message": "Todo not found"}

@router.delete("/{todo_id}")
async def delete_todo_by_id(todo_id: int):
    for todo in todoList:
        if todo.id == todo_id:
            todoList.remove(todo)
            return {"message": "Todo deleted"}
    return {"message": "Todo not found"}