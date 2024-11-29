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

# CREATE: Add a new ride request
def add_ride_request(user_id, pickup, dropoff):
    db = get_mongo_connection()
    db.rides.insert_one({
        "user_id": user_id,
        "pickup": pickup,
        "dropoff": dropoff,
        "status": "Pending",
        "driver_id": None
    })

# UPDATE: Accept a ride
def accept_ride(ride_id, driver_id):
    db = get_mongo_connection()
    db.rides.update_one(
        {"_id": ride_id},
        {"$set": {"status": "Accepted", "driver_id": driver_id}}
    )

# UPDATE: Complete a ride
def complete_ride(ride_id):
    db = get_mongo_connection()
    db.rides.update_one(
        {"_id": ride_id},
        {"$set": {"status": "Completed"}}
    )

# READ: Get rides by status
def get_rides_by_status(status):
    db = get_mongo_connection()
    return list(db.rides.find({"status": status}, {"_id": 0}))
