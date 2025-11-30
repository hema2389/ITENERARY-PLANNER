from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class CrowdDensity(BaseModel):
    location_id: str
    score: int = Field(ge=0, le=100)
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class Destination(BaseModel):
    destination_id: str
    name: str
    description: str
    average_crowd_density: int
    sustainability_score: int
    activities: List[str]

class Feedback(BaseModel):
    feedback_id: str
    user_id: Optional[str] = None
    itinerary_id: str
    crowd_averse_satisfaction: int = Field(ge=1, le=5)
    experience_quality: int = Field(ge=1, le=5)
    comments: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
