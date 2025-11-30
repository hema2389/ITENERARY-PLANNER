from flask import Blueprint, request, jsonify
from firebase_admin import auth
from utils.firestore import add_document, get_document, update_document
from schemas.user import User, Preferences
from middleware.auth import token_required

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/verify', methods=['POST'])
def verify_token():
    """
    Verify the Firebase ID token and create/update the user in Firestore.
    """
    id_token = request.json.get('token')
    if not id_token:
        return jsonify({"error": "ID token is required"}), 400

    try:
        # Verify the ID token
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        email = decoded_token.get('email')

        # Check if the user already exists in Firestore
        user_record = get_document('users', uid)

        if user_record:
            # User exists, update their last login time
            update_document('users', uid, {'updated_at': 'firestore.SERVER_TIMESTAMP'})
        else:
            # New user, create a new user record
            new_user = User(uid=uid, email=email)
            add_document('users', new_user.dict(), document_id=uid)

        return jsonify({"message": "Token verified successfully", "uid": uid}), 200

    except auth.InvalidIdTokenError:
        return jsonify({"error": "Invalid ID token"}), 401
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@auth_bp.route('/user', methods=['GET'])
@token_required
def get_user():
    """
    Get the user's profile information.
    """
    uid = request.user['uid']
    user_data = get_document('users', uid)
    if user_data:
        return jsonify(user_data), 200
    return jsonify({"error": "User not found"}), 404

@auth_bp.route('/user', methods=['PUT'])
@token_required
def update_user():
    """
    Update the user's preferences.
    """
    uid = request.user['uid']
    preferences_data = request.json

    try:
        user_data = get_document('users', uid)
        if not user_data:
            return jsonify({"error": "User not found"}), 404

        # Merge the new preferences with the existing ones
        existing_preferences = user_data.get('preferences', {})
        existing_preferences.update(preferences_data)

        # Validate the updated preferences
        preferences = Preferences(**existing_preferences)

        update_document('users', uid, {'preferences': preferences.dict()})
        return jsonify({"message": "Preferences updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
