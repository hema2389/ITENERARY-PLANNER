from langchain.tools import tool
import requests
from utils.firestore import db

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

@tool
def retrieve_destinations(crowd_threshold: int, sustainability_threshold: int) -> list:
    """
    Retrieves a list of destinations from the database that meet the specified
    crowd and sustainability thresholds.
    """
    try:
        destinations_ref = db.collection('destinations')
        query = destinations_ref.where('average_crowd_density', '<=', crowd_threshold).where('sustainability_score', '>=', sustainability_threshold)
        results = query.stream()

        destinations = [doc.to_dict() for doc in results]
        return destinations
    except Exception as e:
        return [{"error": f"Failed to retrieve destinations: {str(e)}"}]
