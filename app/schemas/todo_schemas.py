from pydantic import BaseModel


class TaskSchema(BaseModel):
    user_id: int
    title: str
    description: str
    is_done: bool