from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from .tools import get_simulated_crowd_data

def get_crowd_density_agent():
    """
    Creates and returns the crowd-density agent executor.
    """
    # Define the tools the agent will have access to
    tools = [get_simulated_crowd_data]

    # Create the system prompt
    system_prompt = """
    You are a crowd-density analysis expert. Your goal is to provide a crowd score from 0 to 100 for a given location based on available data.

    **Instructions:**
    1.  Use the `get_simulated_crowd_data` tool to get data for the location.
    2.  Analyze the foot traffic, event calendar, and weather.
    3.  Calculate a final crowd score (0-100) based on the data. A higher foot traffic number or a scheduled event should increase the score.
    4.  Respond ONLY with the final integer score. For example: `85`.
    """

    # Initialize the LLM
    llm = ChatOpenAI(temperature=0)

    # Create the agent graph
    crowd_density_agent_executor = create_agent(
        model=llm,
        tools=tools,
        system_prompt=system_prompt,
    )
    return crowd_density_agent_executor
