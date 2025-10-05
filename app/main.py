from fastapi import FastAPI, Depends
from app.routes import todo_routes, user_routes
from app.db import ping_db, init_db
from auth import authenticate_user


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
app.include_router(user_routes.router)

@app.on_event("startup")
@app.get("/")
async def root():
    return {"message": "Welcome to my little FastAPI project"}
@app.get("/protected")
async def protected_route(current_user: str = Depends(authenticate_user)):
    return {"message": f"Hello {current_user}, this is a protected route!"}

async def startup_event():
    await ping_db()
    await init_db()