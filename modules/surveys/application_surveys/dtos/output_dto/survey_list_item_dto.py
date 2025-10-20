from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SurveyListItemDTO(BaseModel):
    id: int
    survey_type: str
    farm_name: Optional[str]
    visit_date: Optional[datetime]
    state: Optional[str]
    producter_name: Optional[str]
    extensionist_name: Optional[str]
