from flask import Blueprint, request, jsonify, session
from agents.conversational import get_conversational_agent
from utils.sessions import get_session

chat_bp = Blueprint('chat', __name__, url_prefix='/api/chat')

# In-memory store for conversation agents
conversation_agents = {}

@chat_bp.route('/message', methods=['POST'])
def post_message():
    """
    Processes a user's message and returns the agent's response.
    """
    data = request.get_json()
    message = data.get('message')
    session_id = data.get('session_id')

    if not message:
        return jsonify({"error": "Message is required"}), 400

    user_session = get_session(session_id)
    session_id = user_session['session_id']

    if session_id not in conversation_agents:
        conversation_agents[session_id] = get_conversational_agent()

    agent = conversation_agents[session_id]

    try:
        response = agent.predict(input=message)
        return jsonify({"response": response, "session_id": session_id})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
