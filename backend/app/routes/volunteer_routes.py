from flask import Blueprint, request, jsonify

volunteer_bp = Blueprint('volunteer', __name__)

@volunteer_bp.route('/volunteer', methods=['POST'])
def volunteer():
    """Capture volunteer data."""
    data = request.get_json()
    activity = data.get('activity')
    feedback = data.get('feedback', '')

    # Process the data (store in database or log it)
    # Example: Save to `volunteer` table in the database (not implemented here)

    return jsonify({
        'message': 'Volunteer data captured successfully.',
        'activity': activity,
        'feedback': feedback
    })
