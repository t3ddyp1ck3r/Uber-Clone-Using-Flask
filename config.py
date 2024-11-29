import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev_secret_key')  # Secret key for session management
    DEBUG = os.environ.get('DEBUG', True)  # Debug mode (default: True)
    MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/uber_clone')  # MongoDB connection string
    SESSION_TYPE = 'filesystem'  # Store session data in files
    SESSION_PERMANENT = False    # Session ends when the browser closes
    SESSION_FILE_DIR = os.path.join(os.getcwd(), 'flask_session') # Store session files in a local folder

