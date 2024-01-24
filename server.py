from flask_app.controllers import users
from flask_app.controllers import cars
from flask_app import app
import os

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

# def create_app():
#     if __name__ == "__main__":
#         return app.run(debug=False)