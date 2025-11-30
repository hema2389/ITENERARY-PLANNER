from flask import Blueprint, request, jsonify
from agents.recommender import get_recommendation_agent
import json

recommendations_bp = Blueprint('recommendations', __name__, url_prefix='/api/recommendations')

@recommendations_bp.route('/alternatives', methods=['POST'])
def get_alternatives():
    """
    Gets alternative destinations by invoking the LangChain agent.
    """
    data = request.get_json()

    try:
        agent = get_recommendation_agent()

        # The input to the agent is a JSON string of the user's preferences
        # and the high-crowd POI that needs to be swapped.
        inputs = {"messages": [{"role": "user", "content": json.dumps(data)}]}

        response_chunks = []
        for chunk in agent.stream(inputs, stream_mode="values"):
            response_chunks.append(chunk)

        final_message = response_chunks[-1]['messages'][-1]
        recommendation_json = json.loads(final_message.content)

        return jsonify(recommendation_json)

    except Exception as e:
        return jsonify({"error": f"Failed to get alternatives: {str(e)}"}), 500
