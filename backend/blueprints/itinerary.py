from flask import Blueprint, request, jsonify
from agents.itinerary_generator import get_itinerary_agent
import json

itinerary_bp = Blueprint('itinerary', __name__, url_prefix='/api/itinerary')

@itinerary_bp.route('/generate', methods=['POST'])
def generate_itinerary():
    """
    Generates a complete itinerary by invoking the LangChain agent.
    """
    data = request.get_json()

    try:
        agent = get_itinerary_agent()

        inputs = {"messages": [{"role": "user", "content": json.dumps(data)}]}

        response_chunks = []
        for chunk in agent.stream(inputs, stream_mode="values"):
            response_chunks.append(chunk)

        final_message = response_chunks[-1]['messages'][-1]
        itinerary_json = json.loads(final_message.content)

        return jsonify(itinerary_json)

    except Exception as e:
        return jsonify({"error": f"Failed to generate itinerary: {str(e)}"}), 500

@itinerary_bp.route('/regenerate-day', methods=['POST'])
def regenerate_day():
    """
    Placeholder for regenerating a specific day of an itinerary.
    """
    data = request.get_json()
    # In the future, this will call the LangChain agent
    return jsonify({"message": "Day regeneration placeholder", "data": data})
