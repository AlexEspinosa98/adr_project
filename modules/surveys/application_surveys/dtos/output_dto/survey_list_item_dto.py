from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class SurveyListItemDTO(BaseModel):
    id: int
    survey_type: int
    farm_name: Optional[str]
    visit_date: Optional[datetime]
    state: Optional[str]
    producter_name: Optional[str]
    extensionist_name: Optional[str]
    created_at: Optional[datetime]
    rejection_reason: Optional[str] = None
