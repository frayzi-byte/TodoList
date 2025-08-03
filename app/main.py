from fastapi import FastAPI
from app.routes import todo_routes
from app.db import ping_db, init_db

app = FastAPI(
    title="Library API",
    description="API for managing todolist connection.",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "TodoList",
            "description": "Operations related to tasks: create, list, update, and delete."
        }
    ]
)

app.include_router(todo_routes.router)

@app.on_event("startup")

async def startup_event():
    await ping_db()
    await init_db()