from fastapi import FastAPI
from api.config.dbconnection import models
from api.routers import index

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Application is running at http://localhost:8000/docs"}

# Include all routers here
app.include_router(index.router)
