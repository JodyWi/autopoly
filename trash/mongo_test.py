# mongo_test.py
from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017")
db = client['polytest']  # your database
collection = db['markets']  # your collection

# Test connection
print("Databases:", client.list_database_names())

# Optional: insert a test document
result = collection.insert_one({"name": "BTC-USD", "price": 30000})
print("Inserted ID:", result.inserted_id)

# Query the collection
for doc in collection.find():
    print(doc)
