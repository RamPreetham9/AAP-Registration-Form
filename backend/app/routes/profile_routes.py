from flask import Blueprint, request, jsonify
from ..models import User, db

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/<int:user_id>', methods=['GET'])
def get_profile(user_id):
    """Get user profile by user ID."""
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({
        'id': user.id,
        'unique_member_id': user.unique_member_id,
        'full_name': user.full_name,
        'mobile_number': user.mobile_number,
        'voter_district': user.voter_district,
        'date_of_birth': user.date_of_birth,
        'profile_picture': user.profile_picture
    })

@profile_bp.route('/update/<int:user_id>', methods=['PUT'])
def update_profile(user_id):
    """Update user profile."""
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    user.full_name = data.get('full_name', user.full_name)
    user.voter_district = data.get('voter_district', user.voter_district)
    user.date_of_birth = data.get('date_of_birth', user.date_of_birth)
    db.session.commit()

    return jsonify({'message': 'Profile updated successfully.'})
