from fastapi import APIRouter
from controllers.user_controller import register_user
from models.user_model import UserModel

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/register_user")
async def create_user(user: UserModel):
    await register_user(user)
