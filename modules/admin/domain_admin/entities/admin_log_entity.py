from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class AdminLog(BaseModel):
    id: Optional[int] = Field(None, gt=0)
    admin_user_id: int
    action_id: int
    description: str
    timestamp: Optional[datetime] = None

    class Config:
        from_attributes = True
