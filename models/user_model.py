from pydantic import BaseModel, EmailStr, Field, HttpUrl
from typing import Optional
from datetime import datetime


class UserModel(BaseModel):
    username: str = Field(
        ..., min_length=3, max_length=50, description="The username of the user"
    )
    email: EmailStr = Field(..., description="The email address of the user")
    full_name: Optional[str] = Field(
        None, max_length=100, description="The full name of the user"
    )
    is_active: bool = Field(True, description="Indicates whether the user is active")
    profile_picture: Optional[HttpUrl] = Field(
        None, description="URL to the user's profile picture"
    )
    password: str = Field(..., min_length=6, description="The user's password")
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="The timestamp when the user was created",
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="The timestamp when the user was last updated",
    )
    watch_history: list[str] = Field(
        default_factory=list,
        description="List of Video IDs watched by the user",
    )
    favorite_videos: list[str] = Field(
        default_factory=list,
        description="List of Videos marked as favorite by the user",
    )


class UserInDB(UserModel):
    id: str
    password: str
    created_at: str
    updated_at: str
    access_token: Optional[str] = Field(None)
    refresh_token: Optional[str] = Field(None)

    class Config:
       from_attributes = True
