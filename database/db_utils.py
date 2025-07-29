from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["truthlens"]
reviews_collection = db["reviews"]

def insert_review(doc):
    reviews_collection.insert_one(doc)
