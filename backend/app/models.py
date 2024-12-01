from . import db

# User Model
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
    leader_id = db.Column(db.Integer, nullable=True)  # Optional field for leader assignment
    otp = db.Column(db.String(6), nullable=True)
    otp_expiration = db.Column(db.DateTime, nullable=True)
    verified = db.Column(db.Boolean, default=False)  # To track if the user is verified

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