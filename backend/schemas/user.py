from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

class User(BaseModel):
    uid: str
    email: EmailStr
    geographic_origin: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class Preferences(BaseModel):
    user_id: str
    budget: Optional[float] = None
    crowd_tolerance: int = Field(ge=1, le=10, default=5)
    travel_style: Optional[str] = None
    interests: List[str] = []
