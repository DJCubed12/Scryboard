"""This is the Application Factory and entry point for the Flask application."""

from flask import Flask
from flask_cors import CORS

from sockets import socketio, socketio_bp


def create_app():
    app = Flask(__name__)

    # THIS IS FOR DEV ONLY - REMOVE BEFORE PRODUCTION
    CORS(app, origins=["http://127.0.0.1:4200", "http://localhost:4200"])

    # Add all endpoints to the app
    with app.app_context():
        import endpoints

    app.register_blueprint(socketio_bp)
    socketio.init_app(
        app, cors_allowed_origins=["http://127.0.0.1:4200", "http://localhost:4200"]
    )

    return app


if __name__ == "__main__":
    app = create_app()
    socketio.run(app, debug=True)
