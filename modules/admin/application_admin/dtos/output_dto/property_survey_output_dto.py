from datetime import datetime
from typing import Optional

from pydantic import Field

from common.application import dtos as common_dtos


class PropertySurveyOutputDTO(common_dtos.BaseDTO):
    id: int = Field(..., description="Unique identifier for the survey")
    survey_type: str = Field(
        ..., description="Type of the survey (e.g., 'Survey 1', 'Survey 2')"
    )
    date: Optional[datetime] = Field(None, description="Date of the survey")
    state: Optional[str] = Field(None, description="Status of the survey")
