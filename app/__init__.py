from flask import Flask
from app.model.database import Database

db = Database()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jSLFKJcWI3O5uNW436EaV12NEo'

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app