from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user_schemas import UserCreate, UserSchema
from app.services.user_services import (
    create_user,
    show_users,
    update_user_info,
    delete_user
)
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

from app.schemas.user_schemas import UserCreate, UserSchema

@router.post("/", response_model=UserSchema)
async def create(user: UserCreate):
    new_user = await create_user(user)
    return new_user


@router.get("/", dependencies=[Depends(get_current_user)])
async def get_all():
    return await show_users()

@router.put("/{user_id}", dependencies=[Depends(get_current_user)])
async def update(user_id: int, user: UserSchema):
    updated = await update_user_info(user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated successfully"}

@router.delete("/{user_id}", dependencies=[Depends(get_current_user)])
async def delete(user_id: int):
    deleted = await delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
