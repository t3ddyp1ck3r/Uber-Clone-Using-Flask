from pymongo import MongoClient

def get_mongo_connection():
    client = MongoClient("mongodb+srv://grant12507:password12507@uberclone.1322u.mongodb.net/uber_clone?retryWrites=true&w=majority&authSource=admin&appName=UberClone") # Connect to MongoDB using your connection string.
    db = client["uber_clone"] # Access the specific database called "uber_clone".
    return db # Return the database object so you can use it in other parts of your program.

if __name__ == "__main__":
    db = get_mongo_connection() # Call the function to connect to the database.
    print("Connected to MongoDB!") # Print a success message.