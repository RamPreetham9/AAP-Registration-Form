from flask import Blueprint, request, jsonify
from ..models import User, db

leader_bp = Blueprint('leader', __name__)

@leader_bp.route('/update-leader/<int:user_id>', methods=['PUT'])
def update_leader(user_id):
    """Assign a leader for the user."""
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    leader_id = data.get('leader_id')
    leader = User.query.get(leader_id)
    if not leader:
        return jsonify({'error': 'Leader not found'}), 404

    user.leader_id = leader_id
    db.session.commit()

    return jsonify({'message': 'Leader assigned successfully.'})
