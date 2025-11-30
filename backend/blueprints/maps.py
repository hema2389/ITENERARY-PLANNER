from flask import Blueprint, request, jsonify

maps_bp = Blueprint('maps', __name__, url_prefix='/api/maps')

@maps_bp.route('/geodata', methods=['POST'])
def get_geodata():
    """
    Placeholder for getting geo-data for a list of locations.
    """
    data = request.get_json()
    locations = data.get('locations')

    if not locations:
        return jsonify({"error": "Locations are required"}), 400

    # In the future, this will call a geocoding API
    # For now, we'll return mock data
    mock_geodata = {
        "coordinates": {
            "Eiffel Tower": [48.8584, 2.2945],
            "Louvre Museum": [48.8606, 2.3376],
        },
        "travel_times": [
            {"from": "Eiffel Tower", "to": "Louvre Museum", "time": 15},
        ]
    }

    return jsonify(mock_geodata)
