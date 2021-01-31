import os
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
def connect(collection: str):
    uri = os.getenv('MONGO_URI')
    mongoclient = MongoClient(uri)
    database = mongoclient.jatayu
    return database[collection]
