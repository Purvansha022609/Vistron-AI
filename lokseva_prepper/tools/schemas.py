from pydantic import BaseModel, validator
from typing import Optional

class UPSCPreferences(BaseModel):
    """Schema for the user's UPSC CSE study preferences."""
    target_stage: str       # e.g., 'Prelims', 'Mains', 'Comprehensive'
    subject: str            # e.g., 'Indian Polity', 'Modern History', 'Economy', 'Ethics'
    topic: Optional[str] = None
    time_available_days: Optional[int] = None
    preparation_level: Optional[str] = None

    @validator("target_stage")
    def validate_stage(cls, v):
        stages = ["Prelims", "Mains", "Comprehensive"]
        if v not in stages:
            raise ValueError(f"target_stage must be one of {stages}")
        return v
