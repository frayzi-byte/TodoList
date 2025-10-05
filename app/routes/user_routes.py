from fastapi import APIRouter, HTTPException
from app.schemas.user_schemas import UserSchema
from app.services.user_services import (
    create_user,
    show_users,
    update_user_info,
    delete_user
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/")
async def create(user: UserSchema):
    user_id = await create_user(user)
    return {"id": user_id}

@router.get("/")
async def get_all():
    return await show_users()

@router.put("/{user_id}")
async def update(user_id : int, user : UserSchema):
    updated = await update_user_info(user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated successfully"}

@router.delete("/{user_id}")
async def delete(user_id : int):
    deleted = await delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": " deleted successfully"}