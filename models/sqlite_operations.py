import sqlite3
from models.database import create_connection  

# CREATE: Add a new user
def add_user(username, email, password, role):
    conn = create_connection()  # Establish connection
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO users (username, email, password, role) VALUES (?, ?, ?, ?)
    ''', (username, email, password, role))  # Add user details to the database
    conn.commit()  # Save changes
    conn.close()  # Close connection

# READ: Get a user by username
def get_user_by_username(username):
    conn = create_connection()  # Establish connection
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM users WHERE username = ?
    ''', (username,))  # Fetch user details based on username
    user = cursor.fetchone()  # Fetch the first matching record
    conn.close()  # Close connection
    return user

# UPDATE: Update a user's email
def update_user_email(username, new_email):
    conn = create_connection()  # Establish connection
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE users SET email = ? WHERE username = ?
    ''', (new_email, username))  # Update email for the given username
    conn.commit()  # Save changes
    conn.close()  # Close connection

# DELETE: Remove a user by username
def delete_user(username):
    conn = create_connection()  # Establish connection
    cursor = conn.cursor()
    cursor.execute('''
    DELETE FROM users WHERE username = ?
    ''', (username,))  # Delete the user with the given username
    conn.commit()  # Save changes
    conn.close()  # Close connection

# VALIDATE: Check if username and password are correct
def validate_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM users WHERE username = ? AND password = ?
    ''', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user