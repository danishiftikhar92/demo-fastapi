from config.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Users(Base):
   __tablename__ = "users"

   id = Column(Integer, primary_key=True, index=True)
   name = Column(String)
   email = Column(String, unique=True)
   password = Column(String)

   # relationship with TodoList one to many
   todolist = relationship("TodoList", back_populates="owner")
   
