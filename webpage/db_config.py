from pymongo import MongoClient


# client=  MongoClient("localhost:27017")
# db=    client["test"]
# collection =db['users']


MONGO_URL = "mongodb+srv://sharanya:sharanya331@cluster0.hhle2tv.mongodb.net/"
DB_NAME= "sharanya"
DB_PASSWORD= "sharanya331"



client = MongoClient(MONGO_URL)
db = client[DB_NAME]
users_collection = db['users']