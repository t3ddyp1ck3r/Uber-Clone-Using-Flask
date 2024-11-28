from flask import Flask
from routes.user import user_bp  # User routes
from routes.driver import driver_bp  # Driver routes

app = Flask(__name__)
app.register_blueprint(user_bp, url_prefix='/user')  # Register the user blueprint
app.register_blueprint(driver_bp, url_prefix='/driver')  # Register the driver blueprint

if __name__ == '__main__':
    app.run(debug=True)
