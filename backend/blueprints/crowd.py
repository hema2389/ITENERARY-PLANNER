from flask import Blueprint, request, jsonify
from agents.crowd_density import get_crowd_density_agent

crowd_bp = Blueprint('crowd', __name__, url_prefix='/api/crowd')

@crowd_bp.route('/score', methods=['POST'])
def get_crowd_score():
    """
    Gets the current crowd score for a location by invoking the LangChain agent.
    """
    data = request.get_json()
    location = data.get('location')
    if not location:
        return jsonify({"error": "Location is required"}), 400

    try:
        # Get the agent executor
        crowd_density_agent_executor = get_crowd_density_agent()

        # Prepare the input for the agent
        inputs = {"messages": [{"role": "user", "content": f"what is the crowd score for {location}"}]}

        # Invoke the agent to get the crowd score
        response_chunks = []
        for chunk in crowd_density_agent_executor.stream(inputs, stream_mode="values"):
            response_chunks.append(chunk)

        # Extract the final score from the agent's response
        # The agent's final output is typically in the last message of the 'messages' list
        final_message = response_chunks[-1]['messages'][-1]
        score_str = final_message.content

        score = int(''.join(filter(str.isdigit, score_str)))

        return jsonify({"location": location, "score": score})
    except Exception as e:
        return jsonify({"error": f"Failed to get crowd score: {str(e)}"}), 500


@crowd_bp.route('/forecast', methods=['GET'])
def get_crowd_forecast():
    """
    Placeholder for getting a 7-14 day crowd forecast for a location.
    """
    location = request.args.get('location')
    if not location:
        return jsonify({"error": "Location is required"}), 400

    # In the future, this will call a time-series analysis model
    # For now, we'll return a dummy forecast
    forecast = [
        {"day": i, "score": 50 + i * 5} for i in range(1, 8)
    ]
    return jsonify({"location": location, "forecast": forecast})
