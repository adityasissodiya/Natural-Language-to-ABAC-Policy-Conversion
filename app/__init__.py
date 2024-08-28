from flask import Flask
from flask_cors import CORS

def create_app():
    # Initialize the Flask app
    app = Flask(__name__)

    # Enable CORS (Cross-Origin Resource Sharing) if needed
    CORS(app)

    # Import routes (move all routes to a separate file for better organization)
    from .routes import init_routes
    init_routes(app)

    return app
