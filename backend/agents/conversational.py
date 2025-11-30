from langchain_classic.chains import ConversationChain
from langchain_openai import ChatOpenAI
from langchain_classic.memory import ConversationBufferMemory

def get_conversational_agent():
    """
    Creates and returns a conversational agent.
    """
    # Initialize the LLM
    llm = ChatOpenAI(temperature=0)

    # Initialize memory
    memory = ConversationBuffer_Memory()

    # Create the conversation chain
    conversation_agent = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )

    return conversation_agent
