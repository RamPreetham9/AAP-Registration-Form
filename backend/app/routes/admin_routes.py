from flask import Blueprint, request, jsonify
from ..models import User

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/filter', methods=['GET'])
def filter_users():
    """Filter users by Parliament, Assembly, Mandal, District, and City."""
    parliament = request.args.get('parliament')
    assembly = request.args.get('assembly')
    mandal = request.args.get('mandal')
    district = request.args.get('district')
    city = request.args.get('city')

    query = User.query

    if parliament:
        query = query.filter_by(voter_parliament=parliament)
    if assembly:
        query = query.filter_by(voter_assembly=assembly)
    if mandal:
        query = query.filter_by(voter_mandal=mandal)
    if district:
        query = query.filter_by(voter_district=district)
    if city:
        query = query.filter_by(voter_city=city)

    users = query.all()
    result = [{'id': user.id, 'full_name': user.full_name} for user in users]

    return jsonify(result)
