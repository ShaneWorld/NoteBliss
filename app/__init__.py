from flask import Flask
from flask_session import Session
from flask_wtf import CSRFProtect
from app.extensions import db
from config import Config


def create_app(config_class=Config):

    # Create app
    app = Flask(__name__)

    # Load config
    app.config.from_object(config_class)

    # Enable session control
    Session(app)

    # Global enable csrf protect
    csrf =  CSRFProtect(app)

    # Initialize Flask extensions here
    db.init_app(app)
    
    # Create the database
    with app.app_context():
        # Import models to create
        from app.models.auth import Users
        from app.models.notes import Notes
        db.create_all()

    # Register blueprints here
    
    # homepage module
    from app.main import bp1 as main_bp
    app.register_blueprint(main_bp)

    # auth module
    from app.auth import bp2 as auth_bp
    app.register_blueprint(auth_bp)
    
    # edit module
    from app.edit import bp3 as edit_bp
    app.register_blueprint(edit_bp)

    return app
