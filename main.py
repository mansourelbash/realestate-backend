from fastapi import FastAPI, HTTPException
from typing import List
from pymongo import MongoClient
from pymongo.collection import Collection
from pydantic import BaseModel
from models import Item
from bson import ObjectId

app = FastAPI()

# Define the MongoDB client and collection
client = MongoClient("mongodb+srv://mansourprogrammer:oW9ANgU1tfLQtYnW@cluster0.xqrl7.mongodb.net/?retryWrites=true&w=majority&appName=cluster0")
db = client["polygons_db"]  # Choose your database
collection: Collection = db["polygons"]  # Choose your collection

print("MongoDB connection successful.")


def item_to_dict(item):
    item_dict = item.copy()
    item_dict["_id"] = str(item_dict["_id"])  # Convert ObjectId to string
    return item_dict
# Create
@app.post("/items/", response_model=Item)
def create_item(item_id: int, item: Item):
    if collection.find_one({"_id": item_id}):
        raise HTTPException(status_code=400, detail="Item already exists")
    item_dict = item.dict()
    item_dict["_id"] = item_id
    collection.insert_one(item_dict)
    return item

# Read
@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    item = collection.find_one({"_id": item_id})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item_to_dict(item)

@app.get("/items/", response_model=List[Item])
def read_items():
    items = list(collection.find())
    return [item_to_dict(item) for item in items]
# Update
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    result = collection.replace_one({"_id": item_id}, item.dict())
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# Delete
@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int):
    item = collection.find_one_and_delete({"_id": item_id})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item_to_dict(item)