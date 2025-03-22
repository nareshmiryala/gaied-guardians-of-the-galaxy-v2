from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    
    # Load configuration from Config class
    app.config.from_object(Config)
    
    # Register blueprints
    from .routes import bp as routes_blueprint
    app.register_blueprint(routes_blueprint)
    
    return app