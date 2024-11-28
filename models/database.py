import sqlite3

def create_connection():
    conn = sqlite3.connect('database.db')  # Connect to or create a file named 'database.db'
    return conn  # Return the connection so we can use it later.

def create_tables():
    conn = create_connection()  # Call the 'create_connection' function to connect to the database.
    cursor = conn.cursor()  # Get a "cursor" that allows us to interact with the database

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    # This SQL command creates the table "users" with the specified columns and rules.

    conn.commit()  # Save the changes to the database.
    conn.close()  # Close the connection to free up resources.

if __name__ == "__main__":
    create_tables()  # Call the function to create the table.
