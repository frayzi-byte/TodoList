from pydantic import BaseModel

class TaskSchema(BaseModel):
    id: int
    name: str
    desc: str
    compl: bool
