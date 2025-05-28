import os
from pymongo import MongoClient

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://sharanya:sharanya331@cluster0.hhle2tv.mongodb.net/")
DB_NAME = os.environ.get("DB_NAME", "sharanya")

client = MongoClient(MONGO_URL)
db = client[DB_NAME]
collection = db['users']





# client = MongoClient("mongodb://localhost:27017")      #for connect mongodb
# db = client['mydatabase']
# collection = db['users']