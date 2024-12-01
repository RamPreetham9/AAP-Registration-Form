from flask import Blueprint, request, jsonify

election_bp = Blueprint('election', __name__)

@election_bp.route('/participation', methods=['POST'])
def election_participation():
    """Capture election participation interest."""
    data = request.get_json()
    preferences = data.get('preferences', [])

    # Process the election preferences (store in database or log it)
    # Example: Save to `election_participation` table in the database

    return jsonify({
        'message': 'Election participation captured successfully.',
        'preferences': preferences
    })
