from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from .itinerary_tools import get_crowd_density, search_places, filter_destinations

def get_itinerary_agent():
    """
    Creates and returns the itinerary generation agent.
    """
    tools = [get_crowd_density, search_places, filter_destinations]

    prompt = """
    You are an expert travel planner with a focus on avoiding crowds and finding authentic local experiences.
    Your goal is to create a detailed, day-by-day itinerary based on the user's preferences.

    **Instructions:**
    1.  Use the `search_places` tool to find points of interest for the user's destination.
    2.  For each point of interest, use the `get_crowd_density` tool to get the current crowd score.
    3.  Prioritize places with a crowd score below 60.
    4.  Organize the itinerary by day, suggesting a logical flow of activities.
    5.  Include a mix of popular sites and off-the-beaten-path local experiences.
    6.  For each activity, provide a brief description and the reason for its inclusion (e.g., "low crowd score", "authentic experience").
    7.  Return the final itinerary as a JSON object with a `days` array, where each day is an object with a `day_number` and a list of `activities`.

    **User Preferences:**
    {input}
    """

    llm = ChatOpenAI(temperature=0)

    itinerary_agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=prompt,
    )

    return itinerary_agent
