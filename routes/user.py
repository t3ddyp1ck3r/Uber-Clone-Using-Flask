from flask import Blueprint, request, jsonify, redirect, render_template
from models.sqlite_operations import add_user, get_user_by_username, update_user_email, delete_user, validate_user
from flask import session

user_bp = Blueprint('user', __name__)

@user_bp.route('/add_user', methods=['POST'])
def create_user():
    data = request.json
    add_user(data['username'], data['email'], data['password'], data['role'])
    return jsonify({"message": "User added successfully!"})

@user_bp.route('/get_user/<username>', methods=['GET'])
def get_user(username):
    user = get_user_by_username(username)
    if user:
        # Transform the user tuple into a dictionary for better readability
        user_data = {
            "id": user[0],
            "username": user[1],
            "email": user[2],
            "password": user[3],
            "role": user[4],
            "created_at": user[5]
        }
        return jsonify({"user": user_data})
    else:
        return jsonify({"message": "User not found"}), 404

@user_bp.route('/update_email', methods=['PUT'])
def update_email():
    data = request.json
    update_user_email(data['username'], data['new_email'])  # Update email using the operation function
    return jsonify({"message": f"User {data['username']}'s email updated successfully!"})

@user_bp.route('/delete_user', methods=['DELETE'])
def delete_user_endpoint():
    data = request.json
    delete_user(data['username'])  # Delete the user using the operation function
    return jsonify({"message": f"User {data['username']} deleted successfully!"})

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        user = validate_user(data['username'], data['password'])
        if user:
            session['username'] = user[1]
            return redirect('/')
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@user_bp.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect('/')