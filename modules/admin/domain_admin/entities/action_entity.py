from pydantic import BaseModel, Field
from typing import Optional


class Action(BaseModel):
    id: Optional[int] = Field(None, gt=0)
    action: str
    description: str

    class Config:
        from_attributes = True
