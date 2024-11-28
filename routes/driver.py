from flask import Blueprint, request, jsonify
from models.mongodb_operations import add_driver, get_driver_by_id, update_driver_location, delete_driver

driver_bp = Blueprint('driver', __name__)

# CREATE: Add a new driver
@driver_bp.route('/add_driver', methods=['POST'])
def create_driver():
    data = request.json
    add_driver(data['driver_id'], data['vehicle_model'], data['location'])
    return jsonify({"message": "Driver added successfully!"})

# READ: Get driver by ID
@driver_bp.route('/get_driver/<driver_id>', methods=['GET'])
def get_driver(driver_id):
    driver = get_driver_by_id(driver_id)
    if driver:
        return jsonify({"driver": driver})
    else:
        return jsonify({"message": "Driver not found"}), 404

# UPDATE: Update driver's location
@driver_bp.route('/update_location', methods=['PUT'])
def update_location():
    data = request.json
    update_driver_location(data['driver_id'], data['new_location'])
    return jsonify({"message": f"Driver {data['driver_id']}'s location updated successfully!"})

# DELETE: Remove a driver
@driver_bp.route('/delete_driver', methods=['DELETE'])
def delete_driver_endpoint():
    data = request.json
    delete_driver(data['driver_id'])
    return jsonify({"message": f"Driver {data['driver_id']} deleted successfully!"})
