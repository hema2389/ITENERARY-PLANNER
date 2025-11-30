from langchain.tools import tool
import requests

@tool
def get_crowd_density(location: str) -> dict:
    """
    Gets the crowd density score for a given location.
    """
    try:
        response = requests.post('http://127.0.0.1:5000/api/crowd/score', json={'location': location})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to get crowd density: {str(e)}"}

@tool
def search_places(query: str) -> dict:
    """
    Searches for places of interest.
    """
    # In the future, this will call the Google Places API
    # For now, we'll return dummy data
    return {"results": [
        {"name": "Eiffel Tower", "category": "tourist_attraction"},
        {"name": "Louvre Museum", "category": "museum"},
        {"name": "Notre-Dame Cathedral", "category": "tourist_attraction"},
    ]}

@tool
def filter_destinations(destinations: list, preferences: dict) -> list:
    """
    Filters a list of destinations based on user preferences.
    """
    # In the future, this will implement a more sophisticated filtering logic
    # For now, we'll return the original list
    return destinations
