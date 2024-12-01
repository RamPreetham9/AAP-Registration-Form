from flask import Blueprint, jsonify
from app.models import District, Parliament, Assembly, Mandal, Ward  # Import all models

# Create a blueprint for lists
lists_bp = Blueprint('lists', __name__)

# Get all districts
@lists_bp.route('/districts', methods=['GET'])
def get_districts():
    try:
        districts = District.query.all()  # Fetch all districts
        district_list = [{'id': district.id, 'name': district.name} for district in districts]
        return jsonify(district_list), 200
    except Exception as e:
        print(f"Error occurred while fetching districts: {e}")  # Log the error
        return jsonify({'error': 'Failed to fetch districts', 'details': str(e)}), 500

# Get all parliaments
@lists_bp.route('/parliaments', methods=['GET'])
def get_parliaments():
    try:
        parliaments = Parliament.query.all()  # Fetch all parliaments
        parliament_list = [{'id': parliament.id, 'name': parliament.name} for parliament in parliaments]
        return jsonify(parliament_list), 200
    except Exception as e:
        print(f"Error occurred while fetching parliaments: {e}")  # Log the error
        return jsonify({'error': 'Failed to fetch parliaments', 'details': str(e)}), 500

# Get all assemblies
@lists_bp.route('/assemblies', methods=['GET'])
def get_assemblies():
    try:
        assemblies = Assembly.query.all()  # Fetch all assemblies
        assembly_list = [
            {'id': assembly.id, 'name': assembly.name, 'parliament_id': assembly.parliament_id} 
            for assembly in assemblies
        ]
        return jsonify(assembly_list), 200
    except Exception as e:
        print(f"Error occurred while fetching assemblies: {e}")  # Log the error
        return jsonify({'error': 'Failed to fetch assemblies', 'details': str(e)}), 500

# Get all mandals
@lists_bp.route('/mandals', methods=['GET'])
def get_mandals():
    try:
        mandals = Mandal.query.all()  # Fetch all mandals
        mandal_list = [
            {'id': mandal.id, 'name': mandal.name, 'assembly_id': mandal.assembly_id} 
            for mandal in mandals
        ]
        return jsonify(mandal_list), 200
    except Exception as e:
        print(f"Error occurred while fetching mandals: {e}")  # Log the error
        return jsonify({'error': 'Failed to fetch mandals', 'details': str(e)}), 500

# Get all wards
@lists_bp.route('/wards', methods=['GET'])
def get_wards():
    try:
        wards = Ward.query.all()  # Fetch all wards
        ward_list = [
            {
                'id': ward.id,
                'municipality_name': ward.municipality_name,
                'number_of_wards': ward.number_of_wards,
                'district_id': ward.district_id
            }
            for ward in wards
        ]
        return jsonify(ward_list), 200
    except Exception as e:
        print(f"Error occurred while fetching wards: {e}")  # Log the error
        return jsonify({'error': 'Failed to fetch wards', 'details': str(e)}), 500
