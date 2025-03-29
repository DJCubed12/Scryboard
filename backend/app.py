"""This is the Application Factory and entry point for the Flask application."""

from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    # THIS IS FOR DEV ONLY - REMOVE BEFORE PRODUCTION
    CORS(app, origins=["http://localhost:4200"])

    # Add all endpoints to the app
    with app.app_context():
        import endpoints

        return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
