from langchain.tools import tool
import random

@tool
def get_simulated_crowd_data(location: str) -> dict:
    """
    Simulates fetching real-time crowd data for a given location.
    Returns a dictionary with foot traffic and event calendar data.
    """
    print(f"--- Getting simulated crowd data for {location} ---")
    return {
        "foot_traffic": random.randint(10, 1000),
        "event_calendar": "No major events scheduled" if random.random() > 0.2 else "Local concert nearby",
        "weather": "Sunny"
    }
