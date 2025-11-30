from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime

class IntentTranscript(BaseModel):
    session_id: str
    user_id: Optional[str] = None
    messages: List[Dict[str, Any]]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class Itinerary(BaseModel):
    itinerary_id: str
    user_id: str
    destination: str
    days: List[Dict[str, Any]]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
