from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

mongo_url    =  os.getenv("MONGO_URL")
db_name      =  os.getenv("DB_NAME")
client       =  MongoClient(mongo_url)
db           =  client[db_name]
collection   =  db["users"]