from . import db

# User Model
class User(db.Model):
    __tablename__ = 'users'
    
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    unique_member_id = db.Column(db.String(50), unique=True, nullable=False) 
    full_name = db.Column(db.String(100), nullable=False)  # User's full name
    mobile_number = db.Column(db.String(15), unique=True, nullable=False)  # Mobile number
    country_code = db.Column(db.String(5), nullable=True)  # Country code for mobile number
    password = db.Column(db.String(255), nullable=False)  # Hashed password
    date_of_birth = db.Column(db.Date, nullable=True)  # User's date of birth (optional)
    profile_picture = db.Column(db.String(255), nullable=True)  # URL or path to profile picture (optional)
    isAdmin = db.Column(db.Boolean, default=False)
    leader_id = db.Column(db.Integer, nullable=True)  # Optional field for leader assignment
    otp = db.Column(db.String(6), nullable=True)  # OTP for verification
    otp_expiration = db.Column(db.DateTime, nullable=True)  # OTP expiration timestamp
    verified = db.Column(db.Boolean, default=False)  # To track if the user is verified
    
    def __repr__(self):
        return f"<User {self.full_name}>"

class UserLocation:
    __tablename__ = 'userLocation'

    user_id = db.Column(db.Integer, primary_key=True)
    voter_district = db.Column(db.String(100), nullable=True)  # District name
    voter_parliament = db.Column(db.String(100), nullable=True)  # Parliament constituency name (optional)
    voter_assembly = db.Column(db.String(100), nullable=True)  # Assembly constituency name (optional)
    voter_city = db.Column(db.String(100), nullable=True)  # City name (optional)
    voter_mandal = db.Column(db.String(100), nullable=True)  # Mandal name (optional)
    voter_ward = db.Column(db.String(50), nullable=True)  # Ward number (optional, as text)
    
    def __repr__(self):
        return f"UserLocation {self.name}"
        


# District Model
class District(db.Model):
    __tablename__ = 'districts'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<District {self.name}>"

# Parliament (Lok Sabha Constituency) Model
class Parliament(db.Model):
    __tablename__ = 'parliaments'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Parliament {self.name}>"

# Assembly (MLA Constituency) Model
class Assembly(db.Model):
    __tablename__ = 'assemblies'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    parliament_id = db.Column(db.Integer, db.ForeignKey('parliaments.id'), nullable=False)

    # Relationship to Parliament
    parliament = db.relationship('Parliament', backref=db.backref('assemblies', lazy=True))

    def __repr__(self):
        return f"<Assembly {self.name}>"

# Mandals Model
class Mandal(db.Model):
    __tablename__ = 'mandals'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    assembly_id = db.Column(db.Integer, db.ForeignKey('assemblies.id'), nullable=False)

    # Relationship to Assembly
    assembly = db.relationship('Assembly', backref=db.backref('mandals', lazy=True))

    def __repr__(self):
        return f"<Mandal {self.name}>"

class Ward(db.Model):
    __tablename__ = 'wards'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    municipality_name = db.Column(db.String(255), nullable=False)
    number_of_wards = db.Column(db.Integer, nullable=False)
    district_id = db.Column(db.Integer, db.ForeignKey('districts.id'), nullable=False)

    # Relationship to District
    district = db.relationship('District', backref=db.backref('wards', lazy=True))

    def __repr__(self):
        return f"<Ward {self.municipality_name} ({self.number_of_wards} wards)>"
    

class Volunteering(db.Model):
    __tablename__ = 'volunteering'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    participation_methods = db.Column(db.String(255), nullable=False)  # Comma-separated
    likes_about_party = db.Column(db.Text, nullable=True)  # Optional
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class ElectionParticipation(db.Model):
    __tablename__ = 'election_participation'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    interested_positions = db.Column(db.String(255), nullable=False)  # Comma-separated
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class Complaint(db.Model):
    __tablename__ = 'complaints'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)  # To link the complaint to a user
    district = db.Column(db.String(100), nullable=False)
    municipality = db.Column(db.String(100), nullable=False)
    complaint_text = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.String(255), nullable=True)  # Path to uploaded photo
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
