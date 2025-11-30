from uuid import uuid4

# In-memory session store
sessions = {}

def get_session(session_id):
    """
    Retrieves or creates a new session.
    """
    if session_id not in sessions:
        sessions[session_id] = {'session_id': str(uuid4())}
    return sessions[session_id]

def clear_session(session_id):
    """
    Clears a session.
    """
    if session_id in sessions:
        del sessions[session_id]
