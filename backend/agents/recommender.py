from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from .itinerary_tools import retrieve_destinations

def get_recommendation_agent():
    """
    Creates and returns the recommendation agent.
    """
    tools = [retrieve_destinations]

    prompt = """
    You are an expert in sustainable and off-the-beaten-path travel.
    Your goal is to recommend an alternative destination that is less crowded and more sustainable than the user's original choice.

    **Instructions:**
    1.  Use the `retrieve_destinations` tool to find a list of potential alternative destinations.
    2.  From the list, select the best alternative based on the user's preferences.
    3.  Return the recommended destination as a JSON object.

    **User Preferences:**
    {input}
    """

    llm = ChatOpenAI(temperature=0)

    recommendation_agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=prompt,
    )

    return recommendation_agent
