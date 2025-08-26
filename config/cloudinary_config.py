import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv
import os

load_dotenv()


cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True,
)


def upload_on_cloudinary(local_file_path: str):
    try:
        if not local_file_path:
            raise ValueError("File path not found!")

        response = cloudinary.uploader.upload(local_file_path, resource_type="auto")
        os.remove(local_file_path)

        return response

    except Exception as e:
        print(f"Failed to upload file to Cloudinary: {e}")
        if os.local_file_path and os.path.exists(local_file_path):
            os.remove(local_file_path)
        return None


def delete_from_cloudinary(public_id: str):
    try:
        if not public_id:
            raise ValueError("Public ID not found!")
        result = cloudinary.uploader.destroy(public_id, resource_type="image")
        return result

    except Exception as e:
        print(f"Failed to delete file from Cloudinary: {e}")
        return None
