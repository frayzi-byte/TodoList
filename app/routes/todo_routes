from fastapi import APIRouter, HTTPException
from app.schemas.todo_schemas import TaskSchema
from app.services.todo_services import (
    create_task,
    list_tasks,
    update_task,
    delete_task
)

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.post("/")
async def create(task: TaskSchema):
    task_id = await create_task(task)
    return {"id": task_id}

@router.get("/")
async def get_all():
    return await list_tasks()

@router.put("/{task_id}")
async def update(task_id: int, task: TaskSchema):
    updated = await update_task(task_id, task)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task updated successfully"}

@router.delete("/{task_id}")
async def delete(task_id: int):
    deleted = await delete_task(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": " deleted successfully"}