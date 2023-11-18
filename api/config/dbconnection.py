# Desc: This file is used to create all the tables in the database

from api.models.users import Users
from api.models.todo import TodoList
from api.config.db import engine





# List of all models
models = [Users, TodoList]

# Create all tables
for model in models:
    model.metadata.create_all(bind=engine)





