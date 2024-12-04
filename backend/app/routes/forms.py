# routes/forms.py
from flask import Blueprint, request, jsonify
from ..models import Volunteering, ElectionParticipation, db

forms_bp = Blueprint('forms', __name__)

# Volunteering Submission Route
@forms_bp.route('/volunteering', methods=['POST'])
def submit_volunteering():
    data = request.get_json()
    user_id = data['user_id']

    try:
        # Create a new volunteering record
        # print(data['participation_methods'])
        volunteering = Volunteering(
            user_id=user_id,
            participation_methods=",".join(data.get('participation_methods', [])),
            likes_about_party=data.get('feedback', None)
        )
        db.session.add(volunteering)
        db.session.commit()
        return jsonify({'message': 'Volunteering form submitted successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Election Participation Submission Route
@forms_bp.route('/election-participation', methods=['POST'])
def submit_election_participation():
    print("request",request)
    data = request.get_json()
    user_id = data['user_id']

    print(data)
    try:
        # Create a new election participation record
        election_participation = ElectionParticipation(
            user_id=user_id,
            interested_positions=data.get('interested_positions')
        )
        db.session.add(election_participation)
        db.session.commit()
        return jsonify({'message': 'Election participation form submitted successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
