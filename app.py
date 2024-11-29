from flask import Flask, jsonify, render_template
from dotenv import load_dotenv
from flask_session import Session
import os

from config import Config
from routes.user import user_bp
from routes.driver import driver_bp
from routes.ride import ride_bp

# Load .env variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Load configuration from config.py (before initializing Session)
app.config.from_object(Config)

# Initialize session management
Session(app)

# Register blueprints
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(driver_bp, url_prefix='/driver')
app.register_blueprint(ride_bp, url_prefix='/ride')

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Route not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "An internal error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
