import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

db = SQLAlchemy()

from sqlalchemy import text  # Import text for raw SQL queries

def create_app():
    app = Flask(__name__)

    # MySQL connection string
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        "mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
    ).format(
        username=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        database=os.getenv('DB_DATABASE')
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    print(f"Connecting to database at {app.config['SQLALCHEMY_DATABASE_URI']}")

    db.init_app(app)
    CORS(app)

    # Test database connection
    with app.app_context():
        try:
            with db.engine.connect() as connection:
                result = connection.execute(text("SELECT 1"))  # Use `text` for the query
                print("Database connection successful! Result:", result.scalar())
        except Exception as e:
            print(f"Database connection failed: {e}")

    # Register blueprints (routes)
    from .routes.auth_routes import auth_bp
    from .routes.profile_routes import profile_bp
    from .routes.volunteer_routes import volunteer_bp
    from .routes.election_routes import election_bp
    from .routes.admin_routes import admin_bp
    from .routes.leader_routes import leader_bp
    from .routes.lists import lists_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(profile_bp, url_prefix='/api/profile')
    app.register_blueprint(volunteer_bp, url_prefix='/api/volunteer')
    app.register_blueprint(election_bp, url_prefix='/api/election')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    app.register_blueprint(leader_bp, url_prefix='/api/leader')
    app.register_blueprint(lists_bp, url_prefix='/api/lists')
    
    return app
