from . import db
from flask import current_app

def init_db():
    """Initialize the database and create all tables."""
    with current_app.app_context():
        try:
            db.create_all()
            print("Database initialized successfully!")
        except Exception as e:
            print(f"Error initializing the database: {e}")
