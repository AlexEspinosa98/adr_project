from pydantic import BaseModel, Field
from typing import Optional

class Action(BaseModel):
    id: Optional[int] = Field(None, gt=0)
    name: str

    class Config:
        from_attributes = True
