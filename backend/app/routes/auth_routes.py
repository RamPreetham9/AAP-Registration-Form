from flask import Blueprint, request, jsonify
# from werkzeug.security import generate_password_hash
from twilio.rest import Client  # Twilio library
from ..models import User, db
import os
import bcrypt
from datetime import datetime, timedelta
import random

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    """Registers a new user and triggers OTP generation by calling the send_otp function."""
    data = request.get_json()

    # Validate required fields
    required_fields = ['full_name', 'mobile_number', 'password', 'voter_district', 'country_code']
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({'error': f"Missing required fields: {', '.join(missing_fields)}"}), 400

    # Hash the password
    hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    try:
        # Check if the user already exists
        existing_user = User.query.filter_by(mobile_number=data['mobile_number']).first()
        if existing_user:
            return jsonify({'error': 'User already exists with this mobile number'}), 400

        # Create a new user
        user = User(
            unique_member_id=f"UID-{int.from_bytes(os.urandom(3), 'big')}",
            full_name=data['full_name'],
            mobile_number=data['mobile_number'],
            country_code=data['country_code'],
            password=hashed_password,
            voter_district=data['voter_district'],
            date_of_birth=data.get('date_of_birth'),
            profile_picture=data.get('profile_picture'),
            leader_id=data.get('leader_id'),
            verified=False  # User is unverified initially
        )

        db.session.add(user)
        db.session.commit()

        response = send_otp_internal(data['mobile_number'], data['country_code'])

        if response.get('error'):
            return jsonify({'error': 'Registration successful, but OTP sending failed.', 'details': response['error']}), 500

        return jsonify({'message': 'User registered successfully. OTP sent for verification.', 'user_id': user.id}), 201
    except Exception as e:
        return jsonify({'error': f"Registration failed: {str(e)}"}), 500


@auth_bp.route('/send-otp', methods=['POST'])
def send_otp():
    """API endpoint to trigger OTP generation and sending."""
    data = request.get_json()

    if data['mode']=='ResetPass':
        existing_user = User.query.filter_by(mobile_number=data['mobile_number']).first()
        if ~existing_user:
            return jsonify({'error': 'User doesnt exist with this mobile number'}), 400
    else:
        existing_user = User.query.filter_by(mobile_number=data['mobile_number']).first()
        if existing_user:
            return jsonify({'error': 'User already exists with this mobile number'}), 400

    # Validate mobile number and country code
    if 'mobile_number' not in data or 'country_code' not in data:
        return jsonify({'error': 'Mobile number and country code are required'}), 400


    # Call the internal function to handle OTP generation and sending
    response = send_otp_internal(data['mobile_number'], data['country_code'])
    if response.get('error'):
        return jsonify({'error': response['error']}), 500


    data = request.get_json()
    
    # Validate required fields
    if 'mobile_number' not in data or 'password' not in data:
        return jsonify({'error': 'Mobile number and password are required'}), 400

    try:
        # Fetch user by mobile number
        user = User.query.filter_by(mobile_number=data['mobile_number']).first()
        if not user:
            return jsonify({'error': 'User not found'}), 404

        # Verify password using bcrypt
        if not bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
            return jsonify({'error': 'Invalid password'}), 401

        # Successful login
        return jsonify({'message': 'Login successful', 'user_id': user.id, 'name': user.full_name}), 200
    except Exception as e:
        return jsonify({'error': f"Login failed: {str(e)}"}), 500


@auth_bp.route('/verify-otp', methods=['POST'])
def verify_otp():
    from datetime import datetime

    data = request.get_json()

    # Validate mobile number and OTP
    if 'mobile_number' not in data or 'otp' not in data:
        return jsonify({'error': 'Mobile number and OTP are required'}), 400

    try:
        # Fetch user by mobile number
        user = User.query.filter_by(mobile_number=data['mobile_number']).first()
        if not user:
            return jsonify({'error': 'User not found'}), 404

        # Check if OTP matches and is not expired
        if user.otp != data['otp']:
            return jsonify({'error': 'Invalid OTP'}), 401
        if user.otp_expiration < datetime.utcnow():
            return jsonify({'error': 'OTP has expired'}), 401

        # OTP is valid, mark user as verified
        user.otp = None
        user.otp_expiration = None
        user.verified = True
        db.session.commit()

        return jsonify({'message': 'OTP verified successfully. User is now registered.'}), 200
    except Exception as e:
        return jsonify({'error': f"OTP verification failed: {str(e)}"}), 500



def send_otp_internal(mobile_number, country_code):
    """Internal function to generate and send OTP."""
    try:
        # Generate a random 6-digit OTP
        otp = f"{random.randint(100000, 999999)}"
        expiration_time = datetime.utcnow() + timedelta(minutes=10)

        # Fetch user by mobile number
        user = User.query.filter_by(mobile_number=mobile_number).first()
        if not user:
            return {'error': 'User not found'}

        # Update OTP and expiration
        user.otp = otp
        user.otp_expiration = expiration_time
        db.session.commit()

        # Simulate sending OTP (you can replace this with an SMS gateway)
        print(f"Sending OTP {otp} to {country_code}{mobile_number}")

        return {'message': 'OTP sent successfully'}
    except Exception as e:
        return {'error': str(e)}
