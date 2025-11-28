from fastapi import APIRouter, HTTPException, Depends
from app.schemas.project_schemas import ProjectSchema
from app.services.projects_services import (
    create_project,
)
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/projects",
    tags=["projects"],
    dependencies=[Depends(get_current_user)]
)

@router.post("/")
async def create_project(project : ProjectSchema):
    project_id = await create_project(project)
    return project_id