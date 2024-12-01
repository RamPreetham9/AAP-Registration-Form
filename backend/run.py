from app import create_app
from app.database import init_db

app = create_app()

if __name__ == '__main__':
    init_db()  # Initialize database tables
    app.run(host='0.0.0.0', port=5000)
