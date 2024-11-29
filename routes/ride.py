from flask import Blueprint, request, jsonify
from models.mongodb_operations import add_ride_request, accept_ride, complete_ride, get_rides_by_status

ride_bp = Blueprint('ride', __name__)

# Request a new ride
@ride_bp.route('/request_ride', methods=['POST'])
def request_ride():
    data = request.json
    add_ride_request(data['user_id'], data['pickup'], data['dropoff'])
    return jsonify({"message": "Ride requested successfully!"})

# Accept a ride
@ride_bp.route('/accept_ride', methods=['PUT'])
def accept_ride_route():
    data = request.json
    accept_ride(data['ride_id'], data['driver_id'])
    return jsonify({"message": "Ride accepted!"})

# Complete a ride
@ride_bp.route('/complete_ride', methods=['PUT'])
def complete_ride_route():
    data = request.json
    complete_ride(data['ride_id'])
    return jsonify({"message": "Ride completed!"})

# View rides by status
@ride_bp.route('/rides/<status>', methods=['GET'])
def view_rides_by_status(status):
    rides = get_rides_by_status(status)
    return jsonify({"rides": rides})
