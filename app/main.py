from fastapi import FastAPI
from app.routes import todo_routes, user_routes, projects_routes
from app.routes import auth_routes
from app.db import ping_db, init_db

app = FastAPI(
    title="Library API",
    description="API for managing todolist connection.",
    version="1.0.0",
    openapi_tags=[
        {"name": "TodoList", "description": "Manage your tasks"},
        {"name": "Users", "description": "Manage users"},
        {"name": "Auth", "description": "Authentication and JWT tokens"},
        {"name": "Projects", "description": "Create Projects to Develop"},
    ],
    swagger_ui_init_oauth={
        "usePkceWithAuthorizationCodeGrant": True
    }
)

app.include_router(todo_routes.router)
app.include_router(user_routes.router)
app.include_router(auth_routes.router)
app.include_router(projects_routes.router)

@app.on_event("startup")
async def startup_event():
    await ping_db()
    await init_db()
