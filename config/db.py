# from pymongo import MongoClient
# from pymongo.errors import ConnectionFailure
# from motor.motor_asyncio import AsyncIOMotorClient
# from dotenv import load_dotenv
# import os
# import certifi

# load_dotenv()


# class DBConnection:
#     def __init__(self):
#         self.mongoDb_uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
#         self.database_name = os.getenv("DATABASE_NAME")

#     def get_database_connection(self):
#         try:
#             client = MongoClient(
#                 self.mongoDb_uri,
#                 tlsCAFile=certifi.where(),
#                 serverSelectionTimeoutMS=5000,
#             )
#             client.server_info()
#             db = client[self.database_name]
#             return db
#         except ConnectionFailure as e:
#             print(f"Failed to connect to MongoDB: {e}")
#             raise
#         except Exception as e:
#             print(f"An unexpected error occurred: {e}")
#             raise
#         finally:
#             pass


# db_config = DBConnection()
import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# load env file
load_dotenv()

class DataBaseConfig:
    def __init__(self):
        self.uri = os.getenv("MONGODB_URI")
        self.db_name = os.getenv("DATABASE_NAME")
        self.client = None
        self.db = None

    async def connect(self):
        try:
            self.client = AsyncIOMotorClient(self.uri)
            self.db = self.client[self.db_name]
            print("✅ Database connection established successfully.")
        except Exception as e:
            print(f"❌ Failed to connect database: {e}")
            raise e

    async def disconnect(self):
        if self.client:
            self.client.close()
            print("🔌 Database connection closed.")

# export karo object
db_config = DataBaseConfig()

