# clear_markets.py
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["polytest"]  # replace with your database name
collection = db["markets"]  # replace with your collection name

collection.delete_many({})