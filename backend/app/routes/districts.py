from flask import Blueprint, jsonify
from app.models import District  # Import your District model

# Create a blueprint for districts
districts_bp = Blueprint('districts', __name__)

@districts_bp.route('/', methods=['GET'])
def get_districts():
    try:
        districts = District.query.all()  # Fetch all districts
        district_list = [{'id': district.id, 'name': district.name} for district in districts]
        return jsonify(district_list), 200
    except Exception as e:
        print(f"Error occurred while fetching districts: {e}")  # Log the error
        return jsonify({'error': 'Failed to fetch districts', 'details': str(e)}), 500
