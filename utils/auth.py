from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hashed_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password, hash_password):
    return pwd_context.verify(plain_password, hash_password)


def generate_access_token(data: dict, secret: str, expiry: int) -> str:
    try:
        payload = {
            "sub": data["id"],
            "exp": datetime.utcnow() + timedelta(seconds=expiry),
        }
        return jwt.encode(payload, secret, algorithm="HS256")
    except Exception as e:
        raise ValueError(f"Failed to generate access token: {e}")


def generate_refresh_token(data: dict, secret: str, expiry: int) -> str:
    try:
        payload = {
            "sub": data["id"],
            "exp": datetime.utcnow() + timedelta(seconds=expiry),
        }
        return jwt.encode(payload, secret, algorithm="HS256")
    except Exception as e:
        raise ValueError(f"Failed to generate refresh token: {e}")
