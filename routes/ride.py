from flask import Blueprint, request, jsonify, render_template, redirect
from models.mongodb_operations import add_ride_request, accept_ride, complete_ride, get_rides_by_status
from flask import session

ride_bp = Blueprint('ride', __name__)

# Request a new ride
@ride_bp.route('/request_ride', methods=['GET', 'POST'])
def request_ride():
    if request.method == 'POST':
        data = request.form
        pickup = data.get('pickup', '').strip()
        dropoff = data.get('dropoff', '').strip()

        # Basic validation: Check if fields are empty
        if not pickup or not dropoff:
            error = "Pickup and dropoff locations are required."
            return render_template('request_ride.html', error=error)

        # If validation passes, create the ride request
        add_ride_request(
            user_id=session.get('username'),
            pickup=pickup,
            dropoff=dropoff
        )
        return redirect('/')
    return render_template('request_ride.html')

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

