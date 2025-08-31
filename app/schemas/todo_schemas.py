from pydantic import BaseModel, DateTime
from sqlalchemy import ForeignKey


class TaskSchema(BaseModel):
    id =int
    user_id = int
    title = str
    description = str
    is_done = bool
    created_at = DateTime(timezone=True)
