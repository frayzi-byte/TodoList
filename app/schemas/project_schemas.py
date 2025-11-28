from pydantic import BaseModel

class ProjectSchema(BaseModel):
    id : int
    project_name : str
    project_desc : str