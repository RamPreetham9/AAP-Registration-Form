from . import db

# User Model
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    unique_member_id = db.Column(db.String(50), unique=True, nullable=False)  # Unique member ID
    full_name = db.Column(db.String(100), nullable=False)  # User's full name
    mobile_number = db.Column(db.String(15), unique=True, nullable=False)  # Mobile number
    country_code = db.Column(db.String(5), nullable=True)  # Country code for mobile number
    password = db.Column(db.String(255), nullable=False)  # Hashed password
    voter_district = db.Column(db.String(100), nullable=True)  # District name
    voter_parliament = db.Column(db.String(100), nullable=True)  # Parliament constituency name (optional)
    voter_assembly = db.Column(db.String(100), nullable=True)  # Assembly constituency name (optional)
    voter_city = db.Column(db.String(100), nullable=True)  # City name (optional)
    voter_mandal = db.Column(db.String(100), nullable=True)  # Mandal name (optional)
    voter_ward = db.Column(db.String(50), nullable=True)  # Ward number (optional, as text)
    date_of_birth = db.Column(db.Date, nullable=True)  # User's date of birth (optional)
    profile_picture = db.Column(db.String(255), nullable=True)  # URL or path to profile picture (optional)
    leader_id = db.Column(db.Integer, nullable=True)  # Optional field for leader assignment
    otp = db.Column(db.String(6), nullable=True)  # OTP for verification
    otp_expiration = db.Column(db.DateTime, nullable=True)  # OTP expiration timestamp
    verified = db.Column(db.Boolean, default=False)  # To track if the user is verified
    
    def __repr__(self):
        return f"<User {self.full_name}>"


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