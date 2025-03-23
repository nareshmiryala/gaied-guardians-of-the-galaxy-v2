from flask import Flask

app = Flask(__name__, template_folder='../templates')
app.config.from_object('config')

# Import and register routes
from app import routes

# Register routes with the app
routes.init_app(app)