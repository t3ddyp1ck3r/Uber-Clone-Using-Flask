from models.mongodb import get_mongo_connection

# CREATE: Add a new driver
def add_driver(driver_id, vehicle_model, location):
    db = get_mongo_connection()
    db.drivers.insert_one({
        "driver_id": driver_id,
        "vehicle_model": vehicle_model,
        "location": location,
        "rides": []
    })

# READ: Get a driver by ID
def get_driver_by_id(driver_id):
    db = get_mongo_connection()
    return db.drivers.find_one({"driver_id": driver_id}, {"_id": 0})  # Exclude MongoDB's default _id field

# UPDATE: Update driver's location
def update_driver_location(driver_id, new_location):
    db = get_mongo_connection()
    db.drivers.update_one(
        {"driver_id": driver_id},
        {"$set": {"location": new_location}}
    )

# DELETE: Remove a driver
def delete_driver(driver_id):
    db = get_mongo_connection()
    db.drivers.delete_one({"driver_id": driver_id})
