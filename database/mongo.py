from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client.txt_video_bot

users = db.users
tasks = db.tasks
premium = db.premium
banned = db.banned
