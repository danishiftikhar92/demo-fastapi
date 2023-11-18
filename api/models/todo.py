from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.config.db import Base

class TodoList(Base):
    __tablename__ = "todolist"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String, default="pending")

    # relationship with Users many to one
    owner = relationship("Users", back_populates="todolist")