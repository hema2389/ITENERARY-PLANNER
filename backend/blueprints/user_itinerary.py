from flask import Blueprint, request, jsonify
from middleware.auth import token_required
from utils.firestore import add_document, get_document, update_document
from schemas.travel import Itinerary
from schemas.data import Feedback
import uuid

user_itinerary_bp = Blueprint('user_itinerary', __name__, url_prefix='/api/itinerary/user')

@user_itinerary_bp.route('/save', methods=['POST'])
@token_required
def save_itinerary():
    """
    Saves an itinerary to the user's profile.
    """
    uid = request.user['uid']
    itinerary_data = request.json

    try:
        itinerary_id = str(uuid.uuid4())
        itinerary = Itinerary(itinerary_id=itinerary_id, user_id=uid, **itinerary_data)
        add_document('itineraries', itinerary.dict(), document_id=itinerary_id)
        return jsonify({"message": "Itinerary saved successfully", "itinerary_id": itinerary_id}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@user_itinerary_bp.route('/saved', methods=['GET'])
@token_required
def get_saved_itineraries():
    """
    Retrieves all saved itineraries for the user.
    """
    uid = request.user['uid']
    # This is a placeholder for a more complex query
    # In a real app, you would query the 'itineraries' collection for all documents with the user's uid
    return jsonify([])

@user_itinerary_bp.route('/feedback', methods=['POST'])
@token_required
def submit_feedback():
    """
    Submits feedback for an itinerary.
    """
    uid = request.user['uid']
    feedback_data = request.json
    try:
        feedback_id = str(uuid.uuid4())
        feedback = Feedback(feedback_id=feedback_id, user_id=uid, **feedback_data)
        add_document('feedback', feedback.dict(), document_id=feedback_id)
        return jsonify({"message": "Feedback submitted successfully"}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
