from fastapi import HTTPException
import uvicorn 
from pydantic import BaseModel
from typing import Annotated
from fastapi import FastAPI, File, Form, UploadFile
from fastapi import FastAPI
from pydantic import BaseModel
from bson import ObjectId

app = FastAPI()

class Task(BaseModel):
    id: int
    name: str
    compl: bool

tasks = [

]

@app.get("/tasks")
def read_tasks():
    return tasks

@app.get("tasks/{id}")
def read_task(id: int):
    for task in tasks:
        if task["id"] == id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks")
def create_task(new_task : Task):
    new_task.id = tasks(len) + 1
    tasks.append(new_task)

@app.put("/tasks/{task_id}")
def completed_or_not(task_id: int, updated_task: Task):
    for task in tasks:
        if task["id"] == task_id:
            task["compl"] = updated_task.compl
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message" : "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")