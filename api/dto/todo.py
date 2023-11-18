
from pydantic import BaseModel


class Todo(BaseModel):
    title: str
    description: str
    owner_id: int

class TodoCreate(BaseModel):
    title: str
    description: str
    owner_id: int

class TodoUpdate(BaseModel):
    title: str
    description: str
    owner_id: int
    status: str