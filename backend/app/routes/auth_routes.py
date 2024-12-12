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

    print(data)

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
        print("gonna")
        user = User(
            unique_member_id=f"UID-{int.from_bytes(os.urandom(3), 'big')}",
            full_name=data['full_name'],  # Required
            mobile_number=data['mobile_number'],  # Required
            country_code=data['country_code'],  # Required
            password=hashed_password,  # Required
            voter_district=data['voter_district'],  # Required (district name)
            voter_parliament=data.get('voter_parliament', None),  # Optional
            voter_assembly=data.get('voter_assembly', None),  # Optional
            voter_city=data.get('voter_city', None),  # Optional (newly added)
            voter_mandal=data.get('voter_mandal', None),  # Optional
            voter_ward=data.get('voter_ward', None),  # Optional
            date_of_birth=data.get('date_of_birth', None),  # Optional
            profile_picture=data.get('profile_picture', None),  # Optional
            leader_id=data.get('leader_id', None),  # Optional
            verified=False  # Not verified initially
        )

        print(user)

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
    data = request.get_json()

    # Validate mobile number and new password
    if 'mobile_number' not in data or 'new_password' not in data:
        return jsonify({'error': 'Mobile number and new password are required'}), 400

    try:
        # Fetch user by mobile number
        user = User.query.filter_by(mobile_number=data['mobile_number']).first()
        if not user:
            return jsonify({'error': 'User not found'}), 404

        # Update password
        hashed_password = bcrypt.hashpw(data['new_password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user.password = hashed_password
        db.session.commit()

        return jsonify({'message': 'Password reset successfully!'}), 200
    except Exception as e:
        return jsonify({'error': f"Password reset failed: {str(e)}"}), 500

@auth_bp.route('/complete-registration', methods=['POST'])
def complete_registration():
    data = request.get_json()
    print(data)
    try:
        # user = data.get(user, {})
        p1 = data.get('p1', {})
        p2 = data.get('p2', {})
        p3 = data.get('p3', {})
        user = data.get('user', {})
        # Save data into the database
        # print(user)
        # print(f"Location Data: {p1}")
        # print(f"Election Participation: {p2}")
        # print(f"Volunteering Data: {p3}")

        # Return success response
        return jsonify({"message": "Registration completed successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@auth_bp.route('/verify-otp', methods=['POST'])
def verify_otp():
    data = request.get_json()

    # Validate request
    if 'mobile_number' not in data or 'otp' not in data:
        return jsonify({'error': 'Mobile number and OTP are required'}), 400

    try:
        user = User.query.filter_by(mobile_number=data['mobile_number']).first()
        if not user:
            return jsonify({'error': 'User not found'}), 404

        # Check if OTP matches and is not expired
        if user.otp != data['otp']:
            return jsonify({'error': 'Invalid OTP'}), 401
        if user.otp_expiration < datetime.utcnow():
            return jsonify({'error': 'OTP has expired'}), 401

        # OTP is valid
        user.otp = None
        user.otp_expiration = None
        db.session.commit()

        if not user.verified:
            # Registration case
            user.verified = True
            db.session.commit()
            return jsonify({'message': 'OTP verified successfully. Registration complete.', 'success': True, 'is_registration': True, 'user': {'mobile_number': user.mobile_number}}), 200
        else:
            # Reset password case
            return jsonify({'message': 'OTP verified successfully. Proceed to reset password.', 'success': True, 'is_registration': False}), 200

    except Exception as e:
        return jsonify({'error': f"OTP verification failed: {str(e)}"}), 500

@auth_bp.route('/send-otp', methods=['POST'])
def send_otp():
    """API endpoint to generate and send OTP for user actions."""
    data = request.get_json()

    # Validate required fields
    if 'mobile_number' not in data or 'country_code' not in data:
        return jsonify({'error': 'Mobile number and country code are required'}), 400

    try:
        # Fetch the user by mobile number
        user = User.query.filter_by(mobile_number=data['mobile_number']).first()

        if 'mode' not in data or data['mode'] == "Register":
            # Registration mode: Ensure user does not already exist
            if user:
                return jsonify({'error': 'User already exists. Cannot resend OTP for registration.'}), 400
            # Create a new user if not found
            user = User(
                mobile_number=data['mobile_number'],
                country_code=data['country_code'],
                verified=False  # Not verified initially
            )
            db.session.add(user)
            db.session.commit()
        elif data['mode'] == "ResetPass":
            # Password reset mode: Ensure user exists
            if not user:
                return jsonify({'error': 'User not found. Cannot send OTP for password reset.'}), 404

        # Send OTP
        response = send_otp_internal(data['mobile_number'], data['country_code'])
        if response.get('error'):
            return jsonify({'error': response['error']}), 500

        return jsonify({'message': 'OTP sent successfully'}), 200
    except Exception as e:
        return jsonify({'error': f"Failed to send OTP: {str(e)}"}), 500

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

@auth_bp.route('/login', methods=['POST'])
def login():
    """Login function to authenticate a user using mobile number and password."""
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

        # Ensure user is verified
        if not user.verified:
            return jsonify({'error': 'User is not verified. Please verify OTP first.'}), 403

        # Return user details on successful login
        return jsonify({
            'message': 'Login successful!',
            'user': {
                'id': user.id,
                'full_name': user.full_name,
                'mobile_number': user.mobile_number,
                'voter_district': user.voter_district
            }
        }), 200

    except Exception as e:
        return jsonify({'error': f"Login failed: {str(e)}"}), 500
