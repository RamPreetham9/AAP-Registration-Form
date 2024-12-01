from . import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    unique_member_id = db.Column(db.String(50), unique=True, nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    mobile_number = db.Column(db.String(15), unique=True, nullable=False)
    country_code = db.Column(db.String(5), nullable=True)
    password = db.Column(db.String(255), nullable=False)
    voter_district = db.Column(db.String(100), nullable=True)
    date_of_birth = db.Column(db.Date, nullable=True)
    profile_picture = db.Column(db.String(255), nullable=True)
    leader_id = db.Column(db.Integer, nullable=True)
    otp = db.Column(db.String(6), nullable=True)
    otp_expiration = db.Column(db.DateTime, nullable=True)
    verified = db.Column(db.Boolean, default=False)  # New field to track verification status


class District(db.Model):
    __tablename__ = 'districts'  # Table name in the database

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Primary key
    name = db.Column(db.String(255), nullable=False)  # Name of the district

    def __repr__(self):
        return f"<District {self.name}>"
