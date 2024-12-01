from flask import Blueprint, request, jsonify
# from werkzeug.security import generate_password_hash
from twilio.rest import Client  # Twilio library
from ..models import User, db
from dotenv import load_dotenv
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

# Sending OTP While reseting password
@auth_bp.route('/request-reset-password', methods=['POST'])
def request_reset_password():
    """Trigger OTP for password reset."""
    data = request.get_json()

    # Validate required fields
    if 'mobile_number' not in data or 'country_code' not in data:
        return jsonify({'error': 'Mobile number and country code are required'}), 400

    try:
        # Fetch the user by mobile number
        user = User.query.filter_by(mobile_number=data['mobile_number']).first()
        if not user:
            return jsonify({'error': 'User not found'}), 404

        # Send OTP
        response = send_otp_internal(data['mobile_number'], data['country_code'])
        if response.get('error'):
            return jsonify({'error': response['error']}), 500

        return jsonify({'message': 'OTP sent successfully'}), 200
    except Exception as e:
        return jsonify({'error': f"Failed to send OTP: {str(e)}"}), 500

# patch request will be called if otp is verified
@auth_bp.route('/reset-password', methods=['PATCH'])
def reset_password():
    """Reset the password with OTP verification."""
    data = request.get_json()

    # Validate required fields
    required_fields = ['mobile_number', 'otp', 'new_password']
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({'error': f"Missing required fields: {', '.join(missing_fields)}"}), 400

    try:
        # Fetch the user by mobile number
        user = User.query.filter_by(mobile_number=data['mobile_number']).first()
        if not user:
            return jsonify({'error': 'User not found'}), 404

        # Validate OTP
        if user.otp != data['otp']:
            return jsonify({'error': 'Invalid OTP'}), 401
        if user.otp_expiration < datetime.utcnow():
            return jsonify({'error': 'OTP has expired'}), 401

        # Hash the new password
        hashed_password = bcrypt.hashpw(data['new_password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # Update the user's password and clear OTP fields
        user.password = hashed_password
        user.otp = None
        user.otp_expiration = None
        db.session.commit()

        return jsonify({'message': 'Password reset successfully'}), 200
    except Exception as e:
        return jsonify({'error': f"Failed to reset password: {str(e)}"}), 500

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


# Load environment variables
load_dotenv()

# Twilio credentials from .env file
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

def send_otp_internal(mobile_number, country_code):
    """Internal function to generate and send OTP using Twilio."""
    try:
        # Generate a random 6-digit OTP
        otp = f"{random.randint(100000, 999999)}"
        expiration_time = datetime.utcnow() + timedelta(minutes=10)

        # Fetch user by mobile number
        user = User.query.filter_by(mobile_number=mobile_number).first()
        if not user:
            return {'error': 'User not found'}

        # Update OTP and expiration in the database
        user.otp = otp
        user.otp_expiration = expiration_time
        db.session.commit()

        # Initialize Twilio Client
        print(TWILIO_ACCOUNT_SID)
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        # Send OTP via SMS
        message = client.messages.create(
            body=f"Your OTP is {otp}. It will expire in 10 minutes.",
            from_=TWILIO_PHONE_NUMBER,
            to=f"{country_code}{mobile_number}"
        )

        print(f"OTP sent: {message.sid}")  # Log the message SID for debugging

        return {'message': 'OTP sent successfully'}
    except Exception as e:
        return {'error': f"Failed to send OTP: {str(e)}"}
