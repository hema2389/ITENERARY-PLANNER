from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

class Preferences(BaseModel):
    budget: Optional[float] = None
    crowd_tolerance: int = Field(ge=1, le=10, default=5)
    travel_style: Optional[str] = None
    interests: List[str] = []

class User(BaseModel):
    uid: str
    email: EmailStr
    geographic_origin: Optional[str] = None
    preferences: Preferences = Field(default_factory=Preferences)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
