SESSIONS = {}

def create_session(session_id="default"):
    SESSIONS[session_id] = {"history": [], "preferences": {}}
    return SESSIONS[session_id]

def add_to_session(session_id, role, text):

    if session_id not in SESSIONS:
        create_session(session_id)

    SESSIONS[session_id]["history"].append({
        "role": role,
        "text": text
    })