from flask import Flask
from app.model.database import Database
from flask_login import LoginManager

db = Database()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jSLFKJcWI3O5uNW436EaV12NEo'

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(email):
        return db.get_user(email)
    
    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app