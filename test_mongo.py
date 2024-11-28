from pymongo import MongoClient

try:
    client = MongoClient("mongodb+srv://grant12507:password12507@uberclone.1322u.mongodb.net/uber_clone?retryWrites=true&w=majority&authSource=admin&appName=UberClone")
    db = client["uber_clone"]

    # Insert a document into a collection
    result = db.test_collection.insert_one({"name": "John Doe", "role": "Driver"})
    print("Inserted document ID:", result.inserted_id)

    # List collections again
    print("Collections after insert:", db.list_collection_names())

except Exception as e:
    print("Error connecting to MongoDB:", e)
