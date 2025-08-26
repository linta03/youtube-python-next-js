from config.db import db_config
from fastapi import FastAPI, HTTPException
from models.user_model import UserModel, UserInDB
from utils.auth import (
    generate_access_token,
    generate_refresh_token,
    hashed_password,
    verify_password,
)


user_collection = db_config


async def register_user(user: UserModel):
    # check if user already exists

    if user_collection.find_one({"email": user.email}):
        raise HTTPException(
            status_code=400, detail="User with this email already exists"
        )
    if user_collection.find_one({"username": user.username}):
        raise HTTPException(
            status_code=400, detail="User with this username already exists"
        )

    # prepare data for regitration of user
    hashed_pwd = hashed_password(user.password)
    user_data = user.dict()
    user_data["password"] = hashed_pwd

    print(user)
