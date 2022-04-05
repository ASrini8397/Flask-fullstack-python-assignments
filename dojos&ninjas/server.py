from flask_app import app
from flask_app.controllers import controller_routes
from flask_app.controllers import controller_person

# ...server.py


if __name__ == "__main__":
    app.run(debug=True)