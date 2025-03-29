from flask import current_app


# This example shows that returning a string means flask responds with HTML
# Test it out at: http://localhost:5000/
@current_app.route("/")  # This string defines the URL that calls it
def hello_world():
    return "<p>The backend is working!</p>"


# This example shows that returning a dictionary means flask responds with JSON
# Test it out at: http://localhost:5000/data
@current_app.route("/data")
def fake_data():
    return {"msg": "Hi! This is the backend API speaking!"}


# Example endpoint that uses URL parameters
# Test it out at: http://localhost:5000/echo/whatever_i_put_here_will_be_displayed
@current_app.route("/echo/<message>")
def database_table(message):
    return f"<p>{message}</p>"
